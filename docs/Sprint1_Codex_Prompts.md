# Sprint 1 Codex prompt'ları

Durum: **Öneri; 2026-11-03 itibarıyla günceldir.** Hazırlayan: Ahmet (QA). Dayanak: [Sprint1_Action_Items.md](Sprint1_Action_Items.md) ve [Sprint1_Quality_Report.md](Sprint1_Quality_Report.md). İlgili Issue: [#3](https://github.com/mert494/student-information-system/issues/3).

Her üye kendi bölümündeki prompt'u kendi Codex oturumuna, kendi GitHub hesabıyla yapıştırır. Prompt'lar her commit, push, PR ve merge öncesinde onay ister; Codex'in önerdiği değişikliği onaylamadan önce kontrol edin.

## Sıra

| Adım | Kim | Ne zaman |
| --- | --- | --- |
| 1 | Mert | Hemen; diğerleri bunu bekliyor |
| 2 | Nurefşan, Arda, Barış, Azra | Mert "develop açıldı" yazınca, aynı anda |
| 3 | Ahmet (QA) | 2. adımdaki push'lardan sonra: yeniden kontrol, rapor ve review |
| 4 | Mert | Review'lar onaylanınca: merge |
| 5 | Barış | `develop` → `main` merge edildikten sonra: tag ve release |

Teslim: **5 Kasım 2026, 23:59**.

## 1. adım: Mert

```text
Ben Mert, BM321 SIS projesinde Scrum Master'ım. Repo: mert494/student-information-system (sahibi benim).
Önce AGENTS.md, docs/Git_Workflow.md ve origin/docs/ahmet-sprint1-quality branch'indeki
docs/Sprint1_Action_Items.md dosyasını oku. git fetch --all, git branch -a, gh pr list ve
gh issue list ile güncel durumu kontrol et. gh CLI yoksa kur ve gh auth login ile giriş yap.

Görevler (her adımdan önce ne yapacağını göster ve onayımı al):
1. PR #1'i (docs/sprint1-team-guides -> docs/sprint1-process) merge et.
2. Güncel docs/sprint1-process'ten develop branch'ini oluştur ve push et.
3. gh api ile main ve develop için branch protection uygula: PR zorunlu, en az 1 onay,
   yeni commit'te eski onay düşsün, force push ve silme kapalı. Uygulanan ayarı
   gh api ile tekrar okuyup çıktısını göster.
4. PR #2, #6, #7, #8'in hedefini develop yap (gh pr edit <n> --base develop).
5. PR #4'ü, içeriği PR #1 ile develop'a geldiği için açıklama yorumu yazarak kapat.
6. Benim docs/mert-qa-corrections branch'im için develop'a PR aç. Açıklamada değişen dosyaları
   (Sprint1_Submission_Checklist.md, docs/qa/Mert_QA_Corrections.md, Git_Workflow.md,
   GitHub_Projects_Setup.md, team-guides) listele; reviewer ahmetserdar41 olsun.
   develop ile çakışma varsa göster, kendi dosyalarım dışında bir şeyi değiştirme.
7. .github/ISSUE_TEMPLATE/documentation.md şablonuyla Issue aç ve sahiplerini assignee yap:
   Project Proposal (nsankcc), System Vision and Boundary (nsankcc, ardaberkkara1),
   OpenAPI Draft (ardaberkkara1), Team Roles and RACI (azrayy), Initial Product Backlog (nsankcc).
   Açılan Issue numaralarını ilgili PR açıklamalarına "Related: #n" olarak ekle.
   Açmadan önce kullanıcı adlarını gh api repos/.../collaborators ile doğrula.
8. Reviewer ata: #6 -> ardaberkkara1, #7 -> ahmetserdar41, #8 -> ahmetserdar41 ve nsankcc,
   #2 -> mert494.
9. Bittiğinde ekibe atmam için kısa bir mesaj yaz: develop açıldı, PR'lar develop'a çevrildi,
   açılan Issue numaraları.
Kurallar: main'e doğrudan commit yok, force push yok, her merge için ayrıca onayımı al.
Bu adımda sadece PR #1'i merge et; diğer PR'ları merge etme.
```

## 2. adım: Nurefşan

```text
Ben Nurefşan, BM321 SIS projesinde Product Owner'ım. Branch'im: docs/nurefsan-sprint1-requirements, PR #7.
Önce AGENTS.md'yi, origin/docs/ahmet-sprint1-quality branch'indeki docs/Sprint1_Action_Items.md
içinde "Nurefşan" bölümünü ve docs/Sprint1_Quality_Report.md'deki F-06, F-11, F-12, F-14, F-16
bulgularını oku. F-10 ve F-13'ü zaten yaptım (c7e9d79, 1184b26); onlara dokunma. Belgeler İngilizce kalmalı.

Görevler (her commit/push öncesi diff'i göster ve onayımı al):
1. git fetch origin yap. PR #7'nin hedefi develop olmalı (gh pr view 7). origin/develop'u
   branch'ime merge et. docs/Initial_Backlog_Draft.md çakışmasında İngilizce sürümümü koru,
   çakışma işaretlerini temizle, merge commit'i at. Rebase ve force push yapma.
2. F-06: PB-02 AC4 ve PB-05 AC5'teki "appropriate response" yerine somut sonuç yaz
   (yetkisiz işlem: 403 Forbidden; ön koşul/kontenjan sorunu: 409 Conflict + hata mesajı).
   api/openapi.yaml'daki (origin/docs/arda-sprint1-architecture) yanıtlarla uyumlu olsun.
3. F-11: Vision §2.1'deki dört rolü (Student, Instructor, Administrator, Student Affairs Staff)
   Proposal'daki paydaş tablosu ve backlog ile eşleştir. Proposal'da paydaş adları kalabilir ama
   her paydaşın hangi sistem rolüne karşılık geldiğini tablo/cümleyle yaz. Backlog'daki "user",
   "system administrator", "authorized administrator" ifadelerini bu rollerle değiştir.
4. F-12: "University Management" için ya bir PB maddesi ekle ya da Sprint 1 kapsamı dışında
   olduğunu Proposal ve Vision'da yaz. Hangisini seçeceğini bana sor.
5. F-16: PB-05, PB-06, PB-07 user story'lerine "so that ..." kısmını ekle.
6. docs/System_Vision_and_Boundary.md'nin birleşik hâlini koru; Arda'nın Boundary metnini silme.
7. PR #7 açıklamasına Mert'in açtığı Issue numaralarını "Related: #n" olarak ekle ve
   yaptığım değişiklikleri listele. Issue numarası bilinmiyorsa [TODO] yaz.
```

## 2. adım: Arda

```text
Ben Arda, BM321 SIS projesinde Lead Architect'im. Branch'im: docs/arda-sprint1-architecture, PR #8.
Önce AGENTS.md'yi, origin/docs/ahmet-sprint1-quality branch'indeki docs/Sprint1_Action_Items.md
içinde "Arda" bölümünü ve docs/Sprint1_Quality_Report.md'deki F-18…F-21 bulgularını oku.
git config user.email'in s230204017@ankarabilim.edu.tr olduğunu kontrol et (hesap sorunu çözüldü).

Görevler (her commit/push öncesi diff'i göster ve onayımı al):
1. F-20: docs/System_Vision_and_Boundary.md birleşik hâliyle Nurefşan'ın PR #7'sinde. Bu dosyayı
   kendi branch'imden git rm ile kaldır; PR #8'de yalnızca api/openapi.yaml kalsın.
2. F-18: api/openapi.yaml'a ekle:
   - components.securitySchemes.bearerAuth (type: http, scheme: bearer, bearerFormat: JWT)
   - kök seviyede security: [{bearerAuth: []}]; POST /sessions için security: [] (giriş herkese açık)
   - servers: [{url: http://localhost:8080, description: Local development (placeholder)}]
   - info.license: {name: MIT, identifier: MIT}
   x-security-status ve x-servers-status açıklamalarını güncelle (hâlâ "proposed").
3. F-19: her operasyona tags ekle (Sessions, Students, Courses, Registrations, Grades) ve kökte
   tags listesi tanımla. Ana başarı yanıtlarına sahte değerlerle birer example ekle; gerçek öğrenci
   verisi kullanma. Student, Course, Registration, Grade şemalarına temel alanlar ekle
   (ör. studentNumber, fullName, courseCode, title, credits, term, status, value).
   Rol adları Student, Instructor, Administrator, Student Affairs Staff olsun.
4. npx @redocly/cli lint api/openapi.yaml çalıştır; hata kalmayana kadar düzelt, çıktıyı PR #8
   açıklamasına ekle. Bunun canlı API testi değil, sözleşme doğrulaması olduğunu yaz.
5. PR #8'in hedefi develop olmalı (gh pr view 8). Açıklamaya Mert'in açtığı OpenAPI Issue'sunu
   "Related: #n" olarak ekle; bilinmiyorsa [TODO].
6. F-21 (PR #7 merge edildikten sonra, güncel develop'tan yeni branch docs/arda-sprint1-boundary ile):
   birleşik belgedeki §4.4'e "No external systems are in scope for Sprint 1" kararını ve
   basit bir aktör–SIS etkileşim tablosu ekle; develop'a PR aç.
Uydurma karar yazma; onaylanmamış her şeyi "proposed" olarak işaretle. Force push yapma.
```

## 2. adım: Barış

```text
Ben Barış, BM321 SIS projesinde DevOps sorumlusuyum. Branch'im: docs/baris-sprint1-repository, PR #6.
Önce AGENTS.md, docs/Repository_Setup.md ve origin/docs/ahmet-sprint1-quality branch'indeki
docs/Sprint1_Action_Items.md içinde "Barış" bölümünü oku.

Görevler (her commit/push öncesi diff'i göster ve onayımı al):
1. F-17: Repository_Setup.md'de "İlgili Issue: [TODO]" yerine #5'i, kanıt tablosunda
   "Bu çalışmanın PR'ı" yerine #6'yı yaz; PR/Issue listesini gh pr list ve gh issue list ile güncelle.
2. Erişim tablosunu gh api repos/mert494/student-information-system/collaborators ile doğrula
   ve gerçek çıktıya göre doldur. Yetkim yetmezse komutu ve hatayı yaz, değer uydurma.
3. develop artık var: §4'teki geçici PR hedefini develop olarak güncelle.
   gh api repos/mert494/student-information-system/branches/main/protection ve
   .../branches/develop/protection ile kuralları oku ve kanıt tablosuna özetini ekle
   (PR zorunlu, onay sayısı, force push kapalı). 404 dönerse "koruma yok" yaz.
4. PR #6'nın hedefinin develop olduğunu kontrol et; Issue #5'i açıklamada "Closes #5" yap.
Tag işini şimdi yapma; tüm merge'ler bitince ayrı prompt'la yapılacak.
```

## 2. adım: Azra

```text
Ben Azra, BM321 SIS projesinde Agile Process sorumlusuyum.
Önce AGENTS.md, docs/RACI_Matrix.md, docs/RACI_Matrix.csv, docs/Sprint1_Process_Records.md ve
origin/docs/ahmet-sprint1-quality branch'indeki docs/Sprint1_Action_Items.md içinde "Azra"
bölümünü oku. git fetch origin ile develop'u al.

Görevler (her commit/push öncesi diff'i göster ve onayımı al):
1. gh pr view 4 ile PR #4'ü kontrol et. Mert kapattıysa geç. Kapatmadıysa içeriğinin PR #1 ile
   develop'a geldiğini doğrula ve kapatma yorumunu hazırla; kapatmadan önce onayımı al.
2. origin/develop'tan docs/azra-sprint1-process adında yeni branch aç.
3. Sprint1_Process_Records.md'de "Role Assignment" tablosunu ve toplantı/karar kayıtlarını
   yalnızca bana söyleyeceğim gerçekleşmiş toplantı ve kararlarla doldur. Önce hangi bilgilere
   ihtiyaç olduğunu (tarih, katılımcılar, alınan kararlar) bana sor. Yapılmamış toplantı yazma;
   bilinmeyenler [TODO] kalsın.
4. QA-12 / F-09: Ekip RACI'yi onayladıysa RACI_Matrix.md'ye onay tarihini/Decision ID'yi ve
   Mert–Azra iş bölümünü ekle; Mert'in yükü (5 A, 11 R) konuşulduysa kararı yaz.
   .md ve .csv aynı kalsın (her satırda tek A, en az bir R); değişiklikten sonra iki dosyayı
   karşılaştırıp sonucu göster.
5. develop'a PR aç; açıklamada gerçekten değişen dosyaları yaz, Mert'in açtığı RACI Issue'sunu
   "Related: #n" olarak ekle (bilinmiyorsa [TODO]). Reviewer: mert494.
```

## 3. adım: Ahmet (QA)

Ayrı prompt yok. 2. adımdaki push'lardan sonra QA:

- değişiklikleri yeniden kontrol eder (Redocly lint, RACI MD/CSV eşitliği, `git merge-tree` ile çakışma),
- [Sprint1_Quality_Report.md](Sprint1_Quality_Report.md) ve [Sprint1_Action_Items.md](Sprint1_Action_Items.md) dosyalarını günceller,
- PR #7, PR #8 ve Mert'in PR'ı için review yapar.

## 4. adım: Mert (merge)

```text
Ben Mert. Tüm PR'ların develop'a hedeflendiğini ve en az bir onay aldığını gh pr list ve
gh pr view ile kontrol et. Onaysız veya çakışmalı PR varsa merge etme, bana listele.
Şu sırayla, her biri için ayrı onayımı alarak merge et (merge commit, squash yok):
PR #6 (Barış) -> PR #8 (Arda) -> PR #7 (Nurefşan) -> Azra'nın PR'ı -> benim mert-qa-corrections PR'ım
-> Arda'nın boundary PR'ı varsa -> en son PR #2 (Ahmet QA).
Her merge sonrası develop'ta tek bir docs/System_Vision_and_Boundary.md olduğunu ve
api/openapi.yaml'ın var olduğunu kontrol et.
Sonra develop -> main PR'ı aç ("Sprint 1 submission"), açıklamaya merge edilen PR'ları listele.
Onay gelince merge et. Force push yapma.
```

## 5. adım: Barış (tag)

```text
Ben Barış. git fetch origin yap; origin/main'in son commit'ini göster ve develop -> main PR'ının
merge edildiğini doğrula. Şu komutları hazırla ve onayımla çalıştır:
git tag -a sprint-1 <main commit> -m "Sprint 1 submission"
git push origin sprint-1
gh release create sprint-1 --title "Sprint 1" --notes "<merge edilen PR listesi>"
Release linkini docs/Repository_Setup.md ve docs/Sprint1_Submission_Checklist.md'ye eklemek için
develop'tan yeni branch aç ve PR hazırla.
```
