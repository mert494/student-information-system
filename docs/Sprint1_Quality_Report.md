# Sprint 1 kalite raporu

Durum: **Ara rapor; bağımsız review bekliyor.** Hazırlayan: Ahmet (Quality Assurance and Test Automation Engineer). İlgili Issue: [#3](https://github.com/mert494/student-information-system/issues/3). RACI: S1-13 (A/R), S1-05 / S1-09 (C), S1-14 (R).

Bu rapor yalnızca belge, sözleşme ve repository kanıtı kontrolüdür. Çalışan ürün olmadığından birim, entegrasyon veya E2E testi çalıştırılmamıştır; %50 birim test kapsama hedefi Sprint 3'e aittir ve burada değerlendirilmez. Henüz bulunmayan teslimler `Pending` olarak işaretlenmiştir; dosyası olmayan hiçbir kontrol `Passed` sayılmaz. Merge edilmemiş PR'lardaki belgeler, PR'ın head commit'i üzerinden değerlendirilmiştir.

## 1. Kapsam ve kaynak sürümleri

| Kaynak | Branch / commit | Not |
| --- | --- | --- |
| Repository | `mert494/student-information-system` | İlk kontrol: 2026-11-01; yeniden kontroller: 2026-11-02 (iki tur), 2026-11-03 (iki tur), 2026-11-04 |
| Entegrasyon branch'i | `develop` @ `a2d4579` | PR [#1](https://github.com/mert494/student-information-system/pull/1) (`1f6c6dd`), [#16](https://github.com/mert494/student-information-system/pull/16) (`8f37ba5`) ve [#18](https://github.com/mert494/student-information-system/pull/18) (`a2d4579`) merge edildi: süreç belgeleri, RACI, şablonlar, ekip rehberleri, Mert'in düzeltmeleri |
| Gereksinim belgeleri | `docs/nurefsan-sprint1-requirements` @ `e0226bb` | Proposal, birleşik Vision/Boundary, backlog (EN); PR [#7](https://github.com/mert494/student-information-system/pull/7) → `develop`; onaylı (Ahmet, Mert), çakışma yok |
| OpenAPI taslağı | `docs/arda-sprint1-architecture` @ `a34146b` | Yalnızca `api/openapi.yaml`; PR [#8](https://github.com/mert494/student-information-system/pull/8) → `develop`; onaylı (Ahmet) |
| RACI ve süreç kayıtları | `14-docs-confirm-sprint-1-roles-raci-and-agile-process-division` @ `98e323b` | PR [#17](https://github.com/mert494/student-information-system/pull/17) → `develop`; Mert'in değişiklik isteği açık |
| Repository kurulum belgesi | `docs/baris-sprint1-repository` @ `d948a11` | `docs/Repository_Setup.md`; Issue [#5](https://github.com/mert494/student-information-system/issues/5), PR [#6](https://github.com/mert494/student-information-system/pull/6) → `develop`; `origin/develop` branch'e merge edildi (`99d197a`) |
| `main` | `7072b41` | Yalnızca README, LICENSE, .gitignore |

Sonuç değerleri: `Passed`, `Failed`, `Pending`, `Not applicable (gerekçeli)`.

## 2. Yöntem ve araçlar

| Kontrol türü | Yöntem / araç | Durum |
| --- | --- | --- |
| Belge içeriği | Teslim başlıklarına göre manuel okuma | Uygulandı (mevcut dosyalar) |
| Kapsam tutarlılığı | Proposal, Vision/Boundary ve backlog'da rol, özellik ve kapsam dışı listelerinin çapraz karşılaştırması | Uygulandı (`e0226bb`) |
| RACI tutarlılığı | Python `csv` ile Markdown tablo ↔ CSV satır karşılaştırması (ID, görev adı, atamalar); satır başına A ve R sayımı | Uygulandı (`98e323b`) |
| Ölçülemeyen ifade taraması | `grep` ile "kolay, hızlı, uygun, anlaşılır, appropriate, easy, fast, proper" araması + manuel okuma | Uygulandı (`e0226bb`) |
| GitHub kanıtı | `gh api` ile branch, ruleset, tag, release, Issue, PR, review, collaborator ve commit yazarı sorgusu | Uygulandı (2026-11-04) |
| Entegrasyon | `git merge-tree` ile her açık PR'ın `develop`'a ve birbirine karşı çakışma simülasyonu | Uygulandı |
| Belge bağlantıları | Göreli bağlantıların branch'te var olan dosyalara gittiği `git ls-tree` / `git cat-file` ile; boşluk/çakışma işaretleri `git diff --check` ile | Uygulandı |
| OpenAPI doğrulama | Redocly CLI 2.72.1, iki kural setiyle: `npx redocly lint api/openapi.yaml --extends=spec` (yalnızca OpenAPI 3.1 şartnamesi) ve varsayılan `recommended`; ayrıca PyYAML ile operasyon, `operationId`, güvenlik, örnek, şema ve yanıt envanteri. Node v24.13.1 | Uygulandı (`a34146b`). Bu yalnızca sözleşme doğrulamasıdır; canlı API yok ve test edilmedi |

## 3. Kontrol matrisi

| ID | Teslim | Dosya @ commit | Beklenen kriter | Yöntem | Sonuç | Kanıt / not | Bulgu sahibi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-01 | Project Proposal — başlıklar | `docs/Project_Proposal.md` @ `e0226bb` | Problem, paydaş analizi, çözüm ve beklenen çıktılar, fizibilite/kapsam, varsayım/risk, lisans | Manuel | Passed | Ödevdeki tüm başlıklar karşılanıyor; paydaş → sistem rolü eşleme tablosu eklendi | Nurefşan |
| QA-22 | Project Proposal — kanıt | aynı | Problem tanımı destekleyici kanıta dayanıyor | Manuel | Passed | Mevcut üniversite ÖBS'sinin arayüz ön incelemesi eklendi (`c7e9d79`); anket/görüşme yapılmadığı ve gözlemin sınırlılığı açıkça yazılmış | Nurefşan |
| QA-02 | Lisans seçimi | `LICENSE` @ `7072b41`, Proposal §10 @ `e0226bb` | Lisans dosyası + projeye özgü seçim gerekçesi + ekip kararı | Manuel | Passed | MIT dosyası ve projeye özgü gerekçe var (`1184b26`); OpenAPI'de de `license: MIT` (`a34146b`). Ekip onayı PR #7 review'larıyla | Nurefşan, Arda |
| QA-03 | System Vision | `docs/System_Vision_and_Boundary.md` @ `e0226bb` | Amaç, hedef kullanıcılar, sistem sorumlulukları ve temel işlevler | Manuel | Passed | §1–3 mevcut; PO'nun seçtiği dört sistem rolü (§2.1) ve temel işlevler tanımlı | Nurefşan |
| QA-04 | System Boundary | aynı | Sistem bağlamı ve dış etkileşimler, kapsam içi/dışı, kısıt ve varsayımlar | Manuel | Failed | Aktör ↔ SIS etkileşimleri ve kapsam dışı maddeler var. Dış sistemler/arayüzler ("Confirmed external interactions"), rol–izin matrisi ve onaylı kapsam listesi hâlâ `[TODO]` (7 `[TODO]`). Bulgu F-21 | Arda |
| QA-05 | Kapsam tutarlılığı | Proposal ↔ Vision/Boundary ↔ backlog @ `e0226bb` | Roller ve özellikler belgelerde aynı; backlog'daki iş boundary dışında kalmıyor | Çapraz okuma | Passed | Üç belge aynı dört rolü kullanıyor (Student, Instructor, Administrators, Student Affairs Staff); University Management → Administrators eşlemesi ve özel yönetim işlevlerinin kapsam dışı olduğu yazılı. Kalan tek cümle bulgu F-23'te (P3) | Nurefşan |
| QA-06 | OpenAPI — sözdizimi | `api/openapi.yaml` @ `a34146b` | YAML ayrıştırılır; seçilen OpenAPI sürümüne uygun | Redocly `--extends=spec` | Passed | OpenAPI 3.1.0; şartname kurallarıyla 0 hata. Sürüm dosyada "aday, ekip onaysız" olarak işaretli | Arda |
| QA-07 | OpenAPI — içerik | aynı | Path/HTTP operasyonları, `$ref` çözülür, request/response şemaları, operationId benzersiz, path parametreleri tanımlı, başarı + hata (400/401/403/404) yanıtları, güvenlik tanımı | Redocly `recommended` + PyYAML envanteri | Passed | `recommended`: 0 hata, 1 uyarı (`no-server-example.com`; `localhost` bilinçli yer tutucu). `bearerAuth` + kök `security`, `createSession` için `security: []`, `servers` ve `license` var. 12 operasyonun hepsinde tag; 11'inde sahte örnek (`deleteCurrentSession` 204, gövdesiz). `Registration` şemasında `term`/`status` yok. Bulgu F-19 | Arda |
| QA-08 | OpenAPI ↔ backlog | YAML @ `a34146b` ↔ backlog @ `e0226bb` | PB-01…PB-07'nin yetki/hata senaryoları sözleşmede karşılık bulur | Çapraz okuma | Passed | Her operasyonda `x-backlog-reference`. Backlog'daki somut yanıtlar sözleşmeyle uyumlu: yetkisiz → 403, mükerrer kayıt / kontenjan / ön koşul / pasif öğrenci → 409, geçersiz not → 400 | Arda, Nurefşan |
| QA-09 | RACI — MD ↔ CSV | `docs/RACI_Matrix.md`, `.csv` @ `98e323b` | 16 satırın kimlik, görev adı ve hücreleri aynı | Python karşılaştırma | Passed | 16/16 satır birebir aynı; CSV İngilizceye çevrildi (`72b2f86`), UTF-8 BOM korunmuş | Azra |
| QA-10 | RACI — A/R kuralı | aynı | Her satırda tam bir A, en az bir R; yalnızca R/A/C/I, A/R değerleri | Python sayım | Passed | 16 satırın hepsi kurala uyuyor | Azra |
| QA-11 | RACI — ekip kapsamı | aynı | Altı üyenin tamamı ve resmî rolleri yer alıyor | Manuel | Passed | Altı üye ve roller tabloda var | Azra |
| QA-12 | RACI — onay | aynı + `docs/Sprint1_Process_Records.md` @ `98e323b` | Ekip onay tarihi / karar kaydı | Manuel | Passed | D-01 (RACI) ve D-02 (Mert–Azra iş bölümü), 2026-11-03, altı üye; toplantı MM-01 (WhatsApp, 6/6 katılım). Kayıt "team-reported" ve kanıt linki yok; PR #17 henüz merge edilmedi | Azra, Mert |
| QA-27 | Süreç kayıtlarının doğruluğu | `docs/Sprint1_Process_Records.md` @ `98e323b` | Kayıtlar gerçek ve güncel durumla çelişmiyor | `gh api` + manuel | Failed | MM-01 saati "20:00–21:00 UTC" yazıyor; ekip bilgisine göre 20:00–21:00 Europe/Istanbul. Decision Log altındaki paragraf "ruleset yok, branch'ler korumasız, PR hedefleri karışık" diyor; 2026-11-04'te iki ruleset aktif, `develop` korumalı ve tüm açık PR'lar `develop`'u hedefliyor. Bulgu F-24 | Azra |
| QA-13 | Git-Flow kuralları (yazılı) | `docs/Git_Workflow.md` @ `a2d4579` | `main` / `develop` / `feature` dal modeli, commit biçimi, PR, review, merge, protection kuralları | Manuel | Passed | Tüm başlıklar mevcut; gözlenen ayarlar ile önerilen politika ayrı tutulmuş | Mert |
| QA-14 | Git-Flow — uygulama | GitHub (canlı) | `develop` var; `main`/`develop` korumalı; PR'lar `develop`'a gidiyor | `gh api` | Passed | `develop` var (`a2d4579`). Ruleset'ler: `develop-protection` (PR zorunlu, 1 onay, eski onay düşer, silme/force push yasak) ve `main-protection` (aynı, 2 onay). Açık PR'lar #2, #6, #7, #8, #17 → `develop`; PR #4 kapatıldı | Mert, Barış |
| QA-15 | GitHub erişimi | GitHub (canlı) | Altı üyenin yazma yetkisi var | `gh api` | Passed | `nsnkcc`, `ardaberkkara1`, `ahmetserdar41`, `baryyss-001`, `azrayy`: write; `mert494`: admin (2026-11-04) | Barış |
| QA-16 | Issues / Projects | GitHub (canlı) | Teslimler ve backlog öğeleri için gerçek Issue'lar | `gh issue list` | Failed | Teslim Issue'ları #9–#15 açıldı ve atandı; #3, #5 mevcut. PB-01…PB-07 için Issue yok (yalnızca `GitHub_Projects_Setup.md`'de taslak). Bulgu F-04 | Mert |
| QA-17 | Backlog — alan bütünlüğü | `docs/Initial_Backlog_Draft.md` @ `e0226bb` | Her öğede epic, story, kabul kriteri, öncelik, puan, bağımlılık, sahip | Manuel | Failed | Yedi öğenin yedisinde epic, story, öncelik, puan, bağımlılık ve durum var; PB-05'te "Proposed Owner" alanı yok. Bulgu F-23 | Nurefşan |
| QA-18 | Backlog — test edilebilirlik | aynı | Kabul kriterleri ölçülebilir; olumlu ve olumsuz koşul içeriyor | grep + manuel | Passed | "appropriate response" ifadeleri kalktı; 403 / 409 + hata kodu ve mesajı tanımlı. Yedi story'nin hepsinde "so that" var | Nurefşan |
| QA-19 | Backlog — onay | aynı | PO onayı, ekip tahmini, gerçek atama | Manuel | Pending | PO onayı, ekip tahmini ve atamalar "Pending"; API ve Issue eşlemesi dolduruldu | Nurefşan |
| QA-20 | Teslim checklist'i | `docs/Sprint1_Submission_Checklist.md` @ `a2d4579` | Güncel durum, altı teslim başlığıyla uyum | Manuel | Passed | Altı teslim başlığı eşlenmiş; gerçek PR/review/commit linkleri var; bekleyen kanıtlar "pending" | Mert |
| QA-21 | Release / tag | GitHub (canlı) | İncelenmiş commit'e bağlı Sprint 1 tag'i | `gh api` | Pending | Tag ve release yok; `develop` → `main` merge'ünden sonra bekleniyor | Barış |
| QA-23 | Gereksinim belgelerinin entegrasyonu | `docs/nurefsan-sprint1-requirements` @ `e0226bb` | Belgeler Issue'ya bağlı PR ile onaylı hedefe gidiyor; aynı dosyanın ikinci sürümü oluşmuyor | `git merge-tree` + `gh` | Passed | PR #7 → `develop`, `MERGEABLE`; backlog çakışması `6d92c07` ile çözüldü; PR #8 ile çakışma yok. Backlog #11, #12, #15'e referans veriyor; PR açıklaması Issue bağlamıyor (F-23) | Nurefşan, Mert |
| QA-25 | Vision/Boundary tek belge | PR #7 @ `e0226bb`, PR #8 @ `a34146b` | Teslimin tek, birleşik sürümü var | `git merge-tree` | Passed | PR #8 yalnızca `api/openapi.yaml` içeriyor (`c5425a4`); birleşik belge yalnızca PR #7'de | Arda, Nurefşan |
| QA-26 | Commit kimliği | Tüm açık PR commit'leri | Commit'ler yazarın ekipteki GitHub hesabına bağlı | `gh api` | Failed | Arda'nın commit'leri artık `ardaberkkara1`'e bağlı. Nurefşan'ın `26fc3f4`, `243195e`, `c7e9d79`, `1184b26` commit'leri `nsankcc` hesabına bağlı; ekip hesabı `nsnkcc` (sonraki `69832d5`, `6d92c07`, `e0226bb` doğru). Bulgu F-25 | Nurefşan |
| QA-24 | Repository kurulum belgesi | `docs/Repository_Setup.md` @ `d948a11` | Erişim matrisi, clone/branch adımları, doğrulama adımları, eksikler ve kanıt tablosu; geçerli ve güncel bilgi | Manuel + `gh api` + `git merge-tree` + `git diff --check` | Passed | Belge İngilizce; erişim tablosu `collaborators` çıktısıyla, ruleset tablosu `rulesets/26478727` ve `26478471` çıktısıyla birebir aynı; `develop` hedefi doğru; tag "planned" olarak yazılmış; bağlantılar geçerli, çakışma yok. F-17 kapatıldı | Barış |

Özet: 27 kontrolden 20 `Passed`, 5 `Failed`, 2 `Pending`.

## 4. Bulgular

| ID | Öncelik | Bulgu | Önerilen düzeltme | Sahip | Durum |
| --- | --- | --- | --- | --- | --- |
| F-01 | P1 | System Boundary ve `api/openapi.yaml` yoktu. | — | Arda | Kapatıldı (`e522c95`, PR #8) |
| F-02 | — | İlk raporda üyelerin yazma yetkisi olmadığı yazılmıştı. Bu, kontrolün yanlış GitHub hesabıyla yapılmasından kaynaklanan **hatalı bir bulguydu**; altı üyenin de yetkisi var. | — | Ahmet | Kapatıldı (geri çekildi) |
| F-03 | P1 | `develop` ve branch protection yoktu; yazılı Git-Flow kuralları uygulanmıyordu. | — | Mert, Barış | Kapatıldı (`develop` oluşturuldu, PR #1 `1f6c6dd`; `develop-protection` ve `main-protection` ruleset'leri aktif) |
| F-04 | P2 | Teslimler ve PB-01…PB-07 için Issue yoktu. | PB-01…PB-07 için Issue'lar `GitHub_Projects_Setup.md`'deki taslaklarla açılmalı | Mert | Kısmen (teslim Issue'ları #9–#15 açıldı ve atandı; PB Issue'ları yok) |
| F-05 | P2 | PB-07: "anlaşılır boş durum" ölçülebilir değildi. | — | Nurefşan | Kapatıldı (`26fc3f4`) |
| F-06 | P2 | PB-02 ve PB-05: "appropriate response" ölçülebilir değildi. | — | Nurefşan, Arda | Kapatıldı (`69832d5`, `e0226bb`: 403 / 409 + hata kodu ve mesajı; OpenAPI ile uyumlu) |
| F-07 | P3 | Checklist "Beş resmî teslim" diyordu; "commit edilmedi" satırı güncel değildi. | — | Mert | Kapatıldı (PR #16 `8f37ba5`, PR #18 `a2d4579`) |
| F-08 | P3 | Backlog'da tüm önerilen sahipler Arda idi. | — | Nurefşan, Mert | Kapatıldı (`26fc3f4`) |
| F-09 | P3 | RACI'de Mert 5 satırda A, 11 satırda R; diğer üyelerde A sayısı 1–4. Hata değil, iş yükü bilgisi. | — | Azra | Kapatıldı (bilgi; RACI D-01 ile mevcut hâliyle onaylandı) |
| F-10 | P2 | Proposal'da problem tanımı için kanıt yoktu. | — | Nurefşan | Kapatıldı (`c7e9d79`: ÖBS ön incelemesi; anket yapılmadığı ve sınırlılık açıkça yazılı) |
| F-11 | P2 | Rol adları belgeler arasında farklıydı. | — | Nurefşan, Arda | Kapatıldı (`e0226bb`: dört sistem rolü ve paydaş → rol eşlemesi üç belgede aynı) |
| F-12 | P3 | University Management ihtiyacının backlog karşılığı yoktu. | — | Nurefşan | Kapatıldı (`e0226bb`: Administrators rolüne eşlendi; özel yönetim işlevleri Sprint 1 kapsamı dışında) |
| F-13 | P3 | Lisans gerekçesi geneldi. | — | Nurefşan, Arda | Kapatıldı (`1184b26`) |
| F-14 | P2 | Gereksinim PR'ı Issue'suzdu ve backlog dosyasında hedefle çakışıyordu. | — | Nurefşan, Mert | Kapatıldı (`6d92c07` çakışma çözümü; backlog #11, #12, #15'e referans veriyor) |
| F-15 | P2 | PR #4 `develop`'u atlayarak `main`'i hedefliyordu. | — | Azra, Mert | Kapatıldı (PR #4 kapatıldı; içerik PR #1 ile `develop`'ta) |
| F-16 | P3 | PB-05, PB-06, PB-07'de "so that" yoktu. | — | Nurefşan | Kapatıldı (`69832d5`) |
| F-17 | P3 | `Repository_Setup.md` güncel değil: Issue/PR alanları `[TODO]`, erişim ve ruleset alanları `[TODO]`, "`develop` yoktur" ve "geçici hedef `docs/sprint1-team-guides`" yazıyor. | Issue #5 / PR #6 bağlanmalı; erişim tablosu `gh api` çıktısıyla doldurulmalı; `develop` ve ruleset kanıtı eklenmeli; PR açıklamasına "Closes #5" | Barış | Kapatıldı (`d948a11`, PR #6) |
| F-18 | P2 | OpenAPI'de güvenlik şeması, `security`, `servers` ve `license` yoktu. | — | Arda | Kapatıldı (`a34146b`; `recommended` lint 0 hata) |
| F-19 | P3 | OpenAPI'de örnek, tag ve şema alanları eksikti. | `Registration` şemasına `term`/`status` eklenebilir (PB-05 kararıyla) | Arda, Nurefşan | Kısmen (`c5425a4`, `a34146b`: tüm tag'ler, 11 örnek, temel alanlar) |
| F-20 | P1 | `docs/System_Vision_and_Boundary.md` iki PR'da ayrı sürümlerdeydi. | — | Arda, Nurefşan | Kapatıldı (`c5425a4`: PR #8'den çıkarıldı) |
| F-21 | P2 | Boundary'de dış sistemler/arayüzler ve rol izinleri tanımsız (`[TODO]`). | PR #7 merge edildikten sonra §4.4'e "Sprint 1'de dış sistem yok (proposed)" kararı ve aktör–SIS etkileşim tablosu eklenmeli; rol–izin matrisi "pending" olarak işaretlenmeli | Arda | Açık |
| F-22 | P2 | `e522c95` commit'i ekip dışı `ardaberk00` hesabına bağlıydı. | — | Arda | Kapatıldı (e-posta `ardaberkkara1`'e taşındı; geçmiş yeniden yazılmadı) |
| F-23 | P3 | Backlog'da küçük tutarsızlıklar: PB-05'te "University Management is responsible for defining the enrollment dates" (University Management artık Administrators'a eşli ve özel işlevleri kapsam dışı); PB-05'te "Proposed Owner" alanı yok; rol adı "Administrators" çoğul, diğerleri tekil; PR #7 açıklaması eski ve Issue bağlamıyor. | Cümle "Administrators" ile düzeltilmeli; PB-05'e sahip alanı eklenmeli; rol adı tekilleştirilebilir; PR açıklamasına düzeltmeler ve "Related: #11, #12, #15" eklenmeli | Nurefşan | Yeni |
| F-24 | P2 | `Sprint1_Process_Records.md` @ `98e323b`: MM-01 saati UTC olarak yazılmış (ekip bilgisine göre 20:00–21:00 Europe/Istanbul); Decision Log altındaki paragraf ruleset'lerin olmadığını, branch'lerin korumasız olduğunu ve PR hedeflerinin karışık olduğunu söylüyor, bu 2026-11-04 itibarıyla yanlış. | Saat "2026-11-03 20:00–21:00 Europe/Istanbul (17:00–18:00 UTC)" yapılmalı; paragraf güncel duruma göre düzeltilmeli (iki ruleset aktif, tüm açık PR'lar `develop`'a) | Azra | Yeni |
| F-25 | P2 | Nurefşan'ın `26fc3f4`, `243195e`, `c7e9d79`, `1184b26` commit'leri kişisel Gmail adresiyle atılmış ve ekip dışı `nsankcc` hesabına bağlı; ekip hesabı `nsnkcc`. Bu katkılar ekip hesabında görünmez. | Geçmişi yeniden yazmadan çözüm: Gmail adresi `nsankcc`'den kaldırılıp `nsnkcc`'ye eklenmeli (Settings → Emails). Sonraki commit'ler zaten doğru | Nurefşan | Yeni |

Bulgular için ayrı Issue açılmadı; açılması Mert ile koordineli ve onaya bağlıdır. Issue taslağı için `.github/ISSUE_TEMPLATE/documentation.md` kullanılacak.

## 5. Yeniden kontroller

| Bulgu | Düzeltme PR / commit | Yeniden kontrol tarihi | Sonuç |
| --- | --- | --- | --- |
| F-01 | `26fc3f4` (Proposal, Vision) | 2026-11-02 | Kısmen: Boundary ve OpenAPI bekleniyor |
| F-02 | — (hatalı bulgu) | 2026-11-02 | Geri çekildi; QA-15 `Passed` |
| F-05 | `26fc3f4` | 2026-11-02 | Kapatıldı |
| F-06 | `26fc3f4` | 2026-11-02 | Kısmen; "appropriate response" ifadeleri kaldı |
| F-08 | `26fc3f4` | 2026-11-02 | Kapatıldı |
| F-04, F-07, F-09 | — | 2026-11-02 | Değişiklik yok (F-04: Issue #5 eklendi, teslim Issue'ları hâlâ yok) |
| F-14 | PR #7 | 2026-11-02 | Kısmen; PR açıldı, hedef `main` ve Issue bağlantısı yok |
| F-03 | `81a66a9` (öneri belgesi) | 2026-11-02 | Açık; ayar uygulanmadı, yetki Mert'te |
| F-01 | `e522c95` (PR #8) | 2026-11-03 | Kapatıldı; yeni bulgular F-18…F-22 |
| F-03, F-04, F-07 | — | 2026-11-03 | Değişiklik yok |
| F-11, F-20, F-21 | `243195e` | 2026-11-03 | Kısmen; birleşik Vision/Boundary, rol listesi önerisi, kapsam dışı eşitlendi. PR #8 eski dosyayı hâlâ içeriyor |
| F-14, F-15 | PR #7 hedef değişikliği | 2026-11-03 | Kısmen; PR #7 `docs/sprint1-team-guides`'a çevrildi ancak backlog dosyasında çakışmalı. PR #4 hâlâ `main` |
| F-18, F-19, F-22 | — | 2026-11-03 | Değişiklik yok (`e522c95` hâlâ `ardaberk00` hesabında) |
| F-03 | PR #1 (`1f6c6dd`), ruleset'ler | 2026-11-04 | Kapatıldı; `develop` korumalı (1 onay), `main` korumalı (2 onay) |
| F-04 | Issue #9–#15 | 2026-11-04 | Kısmen; teslim Issue'ları var, PB Issue'ları yok |
| F-07 | PR #16 (`8f37ba5`), PR #18 (`a2d4579`) | 2026-11-04 | Kapatıldı |
| F-06, F-11, F-12, F-14, F-16 | `69832d5`, `6d92c07`, `e0226bb` (PR #7) | 2026-11-04 | Kapatıldı; yeni küçük bulgu F-23 |
| F-10, F-13 | `c7e9d79`, `1184b26` (PR #7) | 2026-11-04 | Kapatıldı |
| F-15 | PR #4 kapatıldı | 2026-11-04 | Kapatıldı |
| F-18, F-20 | `c5425a4`, `a34146b` (PR #8) | 2026-11-04 | Kapatıldı; Redocly `recommended` 0 hata, 1 uyarı |
| F-19 | `c5425a4`, `a34146b` (PR #8) | 2026-11-04 | Kısmen |
| F-22 | Hesap e-posta ayarı | 2026-11-04 | Kapatıldı; `e522c95`, `c5425a4`, `a34146b` → `ardaberkkara1` |
| F-09, QA-12 | `3a18842`, `98e323b` (PR #17) | 2026-11-04 | D-01 / D-02 kaydedildi; yeni bulgu F-24 |
| F-21 | — | 2026-11-04 | Değişiklik yok; PR #7 merge'ünü bekliyor |
| F-17 | `99d197a`, `d948a11` (PR #6) | 2026-11-04 (gece) | Kapatıldı; QA-24 `Passed` |

## 6. Açık riskler ve bekleyen kararlar

- **Barış (QA-21):** F-17 kapatıldı; PR #6 merge'e hazır. `sprint-1` tag'i `develop` → `main` merge'ünden sonra bekleniyor.
- **Azra (F-24):** PR #17'deki yanlış ruleset/PR hedefi paragrafı merge edilirse `develop`'ta hatalı kanıt kalır; merge öncesi düzeltilmeli. Mert'in değişiklik isteği yeni commit'te yeniden değerlendirilmeli.
- **Arda (F-21):** Boundary'nin dış sistemler kısmı PR #7 merge edildikten sonra yeni bir PR ile tamamlanacak.
- **Release:** `develop` → `main` PR'ı `main-protection` nedeniyle 2 onay gerektiriyor; `Git_Workflow.md`'deki öneri 1 onay. Ekip kararıyla eşitlenmeli. Sprint 1 tag'i yok.
- **PB Issue'ları (F-04):** PB-01…PB-07 için Issue açılması teslimde backlog izlenebilirliğini güçlendirir.
- **Onay kayıtları:** D-01 / D-02 ve MM-01 "team-reported"; kanıt linki (ekran görüntüsü vb.) yok.
- **Dil:** `develop`'taki süreç belgeleri ve gereksinim belgeleri İngilizce; bu rapor Türkçe. Teslim dili ekipçe netleştirilmeli.
- OpenAPI 3.1.0 dosyada "aday, ekip onaysız" olarak işaretli; güvenlik politikası "proposed". Ekip farklı bir karar verirse QA-06…QA-08 tekrarlanır.
- Teslim tarihi, takım numarası ve Teams "Sprint 1 Examples" formatı rapora yansıtılmadı [TODO].
- Bu rapor tek kişi tarafından hazırlandı; bağımsız review (öneri: Mert) bekleniyor.
