param([string]$JavaHome = $env:JAVA_HOME)
# Candidate local verifier. Related Sprint 3 Issue: [TODO].
# Restores process environment; downloads/builds stay under this candidate directory.
$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$taskLocal = Join-Path $taskRoot '_local'
$taskLogDirectory = Join-Path $taskLocal 'logs'
$taskEnvironmentNames = @('JAVA_HOME', 'MAVEN_USER_HOME', 'TEMP', 'TMP', 'npm_config_cache')
$taskOriginalEnvironment = @{}
foreach ($name in $taskEnvironmentNames) {
    $taskOriginalEnvironment[$name] = [Environment]::GetEnvironmentVariable($name, 'Process')
}
$taskOriginalLocation = Get-Location

function Invoke-Logged {
    param([string]$Command, [string[]]$CommandArguments, [string]$LogName)
    $taskLogPath = Join-Path $taskLogDirectory $LogName
    & $Command @CommandArguments *> $taskLogPath
    $taskExitCode = $LASTEXITCODE
    Get-Content -LiteralPath $taskLogPath
    if ($taskExitCode -ne 0) {
        throw "Command failed with exit $taskExitCode. See $taskLogPath"
    }
}

try {
    if (-not $JavaHome -or -not (Test-Path -LiteralPath (Join-Path $JavaHome 'bin/java.exe'))) {
        throw 'Pass -JavaHome with an installed JDK 21 directory.'
    }
    $taskJavaVersion = (& (Join-Path $JavaHome 'bin/java.exe') -version 2>&1 | Out-String)
    if ($taskJavaVersion -notmatch 'version "21\.') {
        throw "JDK 21 is required for this verification. Observed: $taskJavaVersion"
    }
    Write-Output $taskJavaVersion
    $taskFileSystem = New-Object -ComObject Scripting.FileSystemObject
    $taskAsciiRoot = $taskFileSystem.GetFolder($taskRoot).ShortPath
    if ($taskAsciiRoot -match '[^\x00-\x7F]') {
        throw 'This Windows JDK needs an ASCII path for agent options. Use an isolated ASCII path or enable an available short-path alias; do not move the active repository.'
    }
    New-Item -ItemType Directory -Path $taskLogDirectory -Force | Out-Null
    $taskTemp = Join-Path $taskAsciiRoot '_local/tmp'
    New-Item -ItemType Directory -Path $taskTemp -Force | Out-Null
    $taskRepository = [System.Security.SecurityElement]::Escape((Join-Path $taskAsciiRoot '_local/m2'))
    $taskSettings = Join-Path $taskLocal 'maven-settings.xml'
    [IO.File]::WriteAllText($taskSettings,
        '<settings xmlns="http://maven.apache.org/SETTINGS/1.2.0"><localRepository>' +
        $taskRepository + '</localRepository></settings>',
        [Text.UTF8Encoding]::new($false))
    $env:JAVA_HOME = $JavaHome
    $env:MAVEN_USER_HOME = Join-Path $taskAsciiRoot '_local/maven-user-home'
    $env:TEMP = $taskTemp
    $env:TMP = $taskTemp
    $env:npm_config_cache = Join-Path $taskAsciiRoot '_local/npm-cache'

    Set-Location -LiteralPath (Join-Path $taskAsciiRoot 'backend')
    Invoke-Logged -Command '.\mvnw.cmd' -CommandArguments @(
        '--settings', '../_local/maven-settings.xml', '-B', '-ntp', '-Dstyle.color=never',
        "-Dunit.coverage.data-file=$taskAsciiRoot/backend/target/jacoco-unit.exec",
        'clean', 'verify'
    ) -LogName 'backend-local-verifier.log'

    Set-Location -LiteralPath (Join-Path $taskRoot 'frontend')
    Invoke-Logged -Command 'npm.cmd' -CommandArguments @('ci', '--no-fund', '--no-audit') -LogName 'npm-ci.log'
    Invoke-Logged -Command 'npm.cmd' -CommandArguments @('run', 'build') -LogName 'frontend-local-build.log'
    Invoke-Logged -Command 'npm.cmd' -CommandArguments @('run', 'test:coverage') -LogName 'frontend-local-tests.log'

    Set-Location -LiteralPath $taskRoot
    Invoke-Logged -Command 'python' -CommandArguments @(
        '-B', '-m', 'unittest', 'discover', '-s', 'scripts/tests', '-v'
    ) -LogName 'coverage-tool-tests.log'
    Invoke-Logged -Command 'python' -CommandArguments @(
        'scripts/verify_coverage.py', 'backend', '--coverage', 'backend/target/site/jacoco/jacoco.xml',
        '--tests', 'backend/target/surefire-reports'
    ) -LogName 'backend-coverage-gate.log'
    Invoke-Logged -Command 'python' -CommandArguments @(
        'scripts/verify_coverage.py', 'frontend', '--coverage', 'frontend/coverage/unit/coverage-summary.json',
        '--tests', 'frontend/reports/unit-junit.xml'
    ) -LogName 'frontend-coverage-gate.log'
}
finally {
    Set-Location -LiteralPath $taskOriginalLocation.Path
    foreach ($name in $taskEnvironmentNames) {
        [Environment]::SetEnvironmentVariable($name, $taskOriginalEnvironment[$name], 'Process')
    }
}
