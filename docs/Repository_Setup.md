# Repository erişimi ve kurulum yönergesi

Durum: **Ekip onayına sunulan öneri; ayar uygulanmadı.** Hazırlayan: Barış. İlgili Issue: [TODO]. RACI: S1-07 (A/R), S1-08 (R), S1-14 (R), S1-15 (A/R), S1-16 (R). Branch, PR, review, merge ve protection kuralları [Git_Workflow.md](Git_Workflow.md) içindedir.

## 1. Repository ve Organization

Repository: [mert494/student-information-system](https://github.com/mert494/student-information-system); public, varsayılan branch `main`. Kontrol 2026-11-02'de `git` ve GitHub'ın herkese açık API'siyle yapıldı. Barış'ın Settings erişimi olmadığından collaborator listesi ve branch kuralları doğrulanmadı.

Repository bir Organization'a değil, `mert494` kişisel hesabına aittir. Bu durumda Settings, collaborator ve branch kurallarını yalnızca repository sahibi değiştirebilir. Organization kararı: [TODO].

## 2. Hesap ve erişim matrisi

Ad–hesap eşlemesi repository kayıtlarından çıkarılmıştır; her üye kendi hesabını onaylamalıdır.

| Üye | GitHub hesabı | Repository erişimi |
| --- | --- | --- |
| Arda | `ardaberkkara1` | [TODO] |
| Barış | `baryyss-001` | Branch oluşturabiliyor; Settings erişimi yok |
| Ahmet | `ahmetserdar41` | [TODO] |
| Mert | `mert494` | Repository sahibi |
| Azra | `azrayy` | [TODO] |
| Nurefşan | `nsnkcc` | [TODO] |

## 3. Ön koşullar

- Kendi GitHub hesabı ve repository erişimi.
- Git; commit kimliği kendi adınız ve GitHub hesabınızla eşleşen e-posta olmalıdır.
- Markdown düzenleyebilen bir metin editörü.
- İsteğe bağlı: GitHub CLI (`gh`). Oturum açma her üyenin kendi işidir; token belgelere veya loglara konmaz.

Teknoloji ve sürüm gereksinimleri henüz belirlenmedi: [TODO — Arda].

## 4. Clone ve branch

```bash
git clone https://github.com/mert494/student-information-system.git
cd student-information-system
git config user.name "<Ad Soyad>"
git config user.email "<GitHub hesabınızla eşleşen e-posta>"
git fetch origin
```

`develop` yoktur. Geçici PR hedefi `docs/sprint1-team-guides` branch'idir; çalışma branch'i de buradan başlatılır:

```bash
git switch -c docs/<ad>-sprint1-<konu> origin/docs/sprint1-team-guides
```

Her branch, commit, push, PR ve merge adımı için ayrı onay gerekir ([AGENTS.md](../AGENTS.md)). `main`'e doğrudan push ve force push yapılmaz.

## 5. Güncel doğrulama adımları

Repository'de uygulama kodu, manifest, CI veya Docker dosyası yoktur; bu nedenle çalıştırma veya test komutu yoktur. GitHub Actions ve %50 birim test kapsamı Sprint 3'e, Docker ile tek komutla başlatma ve deployment final teslime aittir. Belge değişikliklerinde:

1. `git status --short` ile yalnızca görev dosyalarının değiştiğini kontrol edin.
2. `git diff --check` ile boşluk ve çakışma işareti hatalarını kontrol edin.
3. Göreli bağlantıların mevcut dosyalara gittiğini ve tablo sütunlarının tutarlı olduğunu kontrol edin.
4. Sır, token, parola, `.env` veya gerçek öğrenci verisi olmadığını kontrol edin.

## 6. Eksikler

- [TODO] Altı üyenin erişim düzeyleri; repository sahibi tarafından doğrulanmalı.
- [TODO] Organization kararı.
- [TODO] `develop` başlangıç commit'i ve kalıcı PR hedefleri.
- [TODO] Protection/ruleset ayarlarının uygulanması ve kanıtı.
- [TODO] Sprint 1 release/tag adı ve hedef commit'i.

## 7. PR, kural ve release kanıtları

Bu belgenin PR'ı iş akışı kanıtı olarak kullanılır; ayrı test PR'ı açılmaz, `main`'e push denenmez.

| Kanıt | Bağlantı |
| --- | --- |
| Mevcut PR'lar | [#1](https://github.com/mert494/student-information-system/pull/1), [#2](https://github.com/mert494/student-information-system/pull/2), [#4](https://github.com/mert494/student-information-system/pull/4) |
| Mevcut Issue | [#3](https://github.com/mert494/student-information-system/issues/3) |
| Bu çalışmanın PR'ı ve bağımsız review | [TODO] |
| Aktif branch kuralı / ruleset | [TODO] |
| Sprint 1 release/tag | [TODO] |
