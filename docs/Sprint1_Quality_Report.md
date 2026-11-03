# Sprint 1 kalite raporu

Durum: **Ara rapor; bağımsız review bekliyor.** Hazırlayan: Ahmet (Quality Assurance and Test Automation Engineer). İlgili Issue: [#3](https://github.com/mert494/student-information-system/issues/3). RACI: S1-13 (A/R), S1-05 / S1-09 (C), S1-14 (R).

Bu rapor yalnızca belge, sözleşme ve repository kanıtı kontrolüdür. Çalışan ürün olmadığından birim, entegrasyon veya E2E testi çalıştırılmamıştır; %50 birim test kapsama hedefi Sprint 3'e aittir ve burada değerlendirilmez. Henüz bulunmayan teslimler `Pending` olarak işaretlenmiştir; dosyası olmayan hiçbir kontrol `Passed` sayılmaz.

## 1. Kapsam ve kaynak sürümleri

| Kaynak | Branch / commit | Not |
| --- | --- | --- |
| Repository | `mert494/student-information-system` | İlk kontrol: 2026-11-01; yeniden kontroller: 2026-11-02 (iki tur), 2026-11-03 (iki tur) |
| Süreç belgeleri | `docs/sprint1-process` @ `78febb9` | RACI, Git_Workflow, backlog taslağı (TR), checklist, şablonlar |
| Ekip rehberleri + süreç kayıtları | `docs/sprint1-team-guides` @ `79e3d40` | PR [#1](https://github.com/mert494/student-information-system/pull/1) ve [#4](https://github.com/mert494/student-information-system/pull/4), açık |
| Gereksinim belgeleri | `docs/nurefsan-sprint1-requirements` @ `243195e` | Proposal, birleşik Vision/Boundary, backlog (EN); PR [#7](https://github.com/mert494/student-information-system/pull/7) → `docs/sprint1-team-guides` (GitHub: çakışmalı) |
| Mimari taslakları | `docs/arda-sprint1-architecture` @ `e522c95` | `api/openapi.yaml` (514 satır), `docs/System_Vision_and_Boundary.md` (Boundary); PR [#8](https://github.com/mert494/student-information-system/pull/8) → `docs/sprint1-team-guides` |
| Repository kurulum belgesi | `docs/baris-sprint1-repository` @ `81a66a9` | `docs/Repository_Setup.md`; Issue [#5](https://github.com/mert494/student-information-system/issues/5), PR [#6](https://github.com/mert494/student-information-system/pull/6) → `docs/sprint1-team-guides` |
| `main` | `7072b41` | Yalnızca README, LICENSE, .gitignore |

Sonuç değerleri: `Passed`, `Failed`, `Pending`, `Not applicable (gerekçeli)`.

## 2. Yöntem ve araçlar

| Kontrol türü | Yöntem / araç | Durum |
| --- | --- | --- |
| Belge içeriği | Teslim başlıklarına göre manuel okuma | Uygulandı (mevcut dosyalar) |
| Kapsam tutarlılığı | Proposal, Vision/Boundary ve backlog'da rol, özellik ve kapsam dışı listelerinin çapraz karşılaştırması | Uygulandı (`26fc3f4`) |
| RACI tutarlılığı | Python `csv` ile Markdown tablo ↔ CSV satır karşılaştırması; satır başına A ve R sayımı | Uygulandı |
| Ölçülemeyen ifade taraması | `grep` ile "kolay, hızlı, uygun, anlaşılır, appropriate, easy, fast, proper" araması + manuel okuma | Uygulandı |
| GitHub kanıtı | `gh api` ile branch, protection, tag, release, Issue, PR, collaborator ve contributor sorgusu | Uygulandı |
| Belge bağlantıları | Göreli bağlantıların branch'te var olan dosyalara gittiği `git cat-file` ile; boşluk/çakışma işaretleri `git diff --check` ile | Uygulandı (`81a66a9`) |
| OpenAPI doğrulama | Redocly CLI 2.72.1, iki kural setiyle: `npx redocly lint api/openapi.yaml --extends=spec` (yalnızca OpenAPI 3.1 şartnamesi) ve varsayılan `recommended`; ayrıca PyYAML ile operasyon, `operationId`, path parametresi, şema ve yanıt envanteri. Node v24.13.1 | Uygulandı (`e522c95`). Bu yalnızca sözleşme doğrulamasıdır; canlı API yok ve test edilmedi |

## 3. Kontrol matrisi

| ID | Teslim | Dosya @ commit | Beklenen kriter | Yöntem | Sonuç | Kanıt / not | Bulgu sahibi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-01 | Project Proposal — başlıklar | `docs/Project_Proposal.md` @ `26fc3f4` | Problem, paydaş analizi, çözüm ve beklenen çıktılar, fizibilite/kapsam, varsayım/risk, lisans | Manuel | Passed | 12 bölüm; ödevdeki tüm başlıklar karşılanıyor | Nurefşan |
| QA-22 | Project Proposal — kanıt | aynı | Problem tanımı destekleyici kanıta dayanıyor | Manuel | Failed | Bölüm 2 problemlerin doğrulanmamış varsayım olduğunu açıkça belirtiyor; kaynak, anket veya gözlem yok. Bulgu F-10 | Nurefşan |
| QA-02 | Lisans seçimi | `LICENSE` @ `7072b41`, Proposal §10 | Lisans dosyası + projeye özgü seçim gerekçesi + ekip kararı | Manuel | Pending | MIT dosyası ve genel açıklama var; projeye özgü gerekçe ve ekip kararı yok. Bulgu F-13 | Nurefşan, Arda |
| QA-03 | System Vision | `docs/System_Vision_and_Boundary.md` @ `243195e` | Amaç, hedef kullanıcılar, sistem sorumlulukları ve temel işlevler | Manuel | Passed | §1–3 mevcut; kullanıcı grupları, önerilen 4 sistem rolü (§2.1) ve 6 işlev tanımlı | Nurefşan |
| QA-04 | System Boundary | `docs/System_Vision_and_Boundary.md` @ `243195e` (birleşik; Boundary içeriği Arda'nın `e522c95` sürümünden) | Sistem bağlamı ve dış etkileşimler, kapsam içi/dışı, kısıt ve varsayımlar | Manuel | Failed | §4.1–4.6 mevcut; aktör ↔ SIS etkileşimleri (§4.4) ve beş kapsam dışı madde (§5.2) artık var. Dış sistemler, arayüzler ve rol izinleri hâlâ `[TODO]`; belgede 7 `[TODO]` kaldı. Bulgu F-21 | Arda |
| QA-05 | Kapsam tutarlılığı | Proposal @ `26fc3f4` ↔ Vision/Boundary @ `243195e` ↔ backlog @ `26fc3f4` | Roller ve özellikler belgelerde aynı; backlog'daki iş boundary dışında kalmıyor | Çapraz okuma | Failed | Kapsam dışı listeleri artık Proposal ile birleşik belgede aynı; backlog'da kapsam dışı iş yok. Rol listesi önerildi ancak "Administrator" ile "University Management" ilişkisi belirsiz ve bir özelliğin backlog karşılığı yok. Bulgu F-11, F-12 | Nurefşan, Arda |
| QA-06 | OpenAPI — sözdizimi | `api/openapi.yaml` @ `e522c95` | YAML ayrıştırılır; seçilen OpenAPI sürümüne uygun | Redocly `--extends=spec` | Passed | OpenAPI 3.1.0; şartname kurallarıyla 0 hata. Sürüm dosyada "aday, ekip onaysız" olarak işaretli | Arda |
| QA-07 | OpenAPI — içerik | aynı | Path/HTTP operasyonları, `$ref` çözülür, request/response şemaları, operationId benzersiz, path parametreleri tanımlı, başarı + hata (400/401/403/404) yanıtları, güvenlik tanımı | Redocly `recommended` + PyYAML envanteri | Failed | 12 operasyon, 11 şema, 6 ortak hata yanıtı; `operationId`'ler benzersiz, `$ref`'ler çözülüyor, path parametreleri `components/parameters` ile tanımlı, her operasyonda 401/500 ve uygun 400/403/404/409 var. `recommended`: 13 hata (12× `security-defined`, 1× `no-empty-servers`) + 1 uyarı (`info-license`); hiç `example` ve `tags` yok. Bulgu F-18, F-19 | Arda |
| QA-08 | OpenAPI ↔ backlog | YAML @ `e522c95` ↔ backlog @ `26fc3f4` | PB-01…PB-07'nin yetki/hata senaryoları sözleşmede karşılık bulur | Çapraz okuma | Passed | Her operasyonda `x-backlog-reference`: PB-01 `/sessions`, PB-03 `/students`, PB-04 `/courses`, PB-05 `/registrations`, PB-06 `PUT /registrations/{registrationId}/grade`, PB-07 `/grades`. PB-02 ayrı endpoint değil; 401/403 yanıtlarıyla karşılanıyor. Mükerrer kayıt → 409, geçersiz not → 400 | Arda, Nurefşan |
| QA-09 | RACI — MD ↔ CSV | `docs/RACI_Matrix.md`, `.csv` @ `78febb9` | 16 satırın kimlik ve hücreleri aynı | Python karşılaştırma | Passed | 16/16 satır birebir aynı; `79e3d40` RACI dosyalarını değiştirmedi | Azra |
| QA-10 | RACI — A/R kuralı | aynı | Her satırda tam bir A, en az bir R; yalnızca R/A/C/I, A/R değerleri | Python sayım | Passed | 16 satırın hepsi kurala uyuyor | Azra |
| QA-11 | RACI — ekip kapsamı | aynı | Altı üyenin tamamı ve resmî rolleri yer alıyor | Manuel | Passed | Altı üye ve roller tabloda var | Azra |
| QA-12 | RACI — onay | aynı + `docs/Sprint1_Process_Records.md` @ `79e3d40` | Ekip onay tarihi / karar kaydı | Manuel | Pending | Onay tarihi `[TODO]`; yeni "Role Assignment" tablosu boş (`[TODO]`) | Azra, Mert |
| QA-13 | Git-Flow kuralları (yazılı) | `docs/Git_Workflow.md` @ `78febb9` | `main` / `develop` / `feature` dal modeli, commit biçimi, PR, review, merge, protection kuralları | Manuel | Passed | Tüm başlıklar mevcut; belge "onaysız taslak" olarak işaretli | Mert |
| QA-14 | Git-Flow — uygulama | GitHub (canlı) | `develop` var; `main`/`develop` korumalı; PR'lar `develop`'a gidiyor | `gh api` | Failed | `develop` yok; hiçbir branch korumalı değil; PR #4 ve #7 doğrudan `main`'i hedefliyor. Bulgu F-03, F-15 | Mert, Barış |
| QA-15 | GitHub erişimi | GitHub (canlı) | Altı üyenin yazma yetkisi var | `gh api` | Passed | `nsnkcc`, `ardaberkkara1`, `ahmetserdar41`, `baryyss-001`, `azrayy`: write; `mert494`: admin | Barış |
| QA-16 | Issues / Projects | GitHub (canlı) | Teslimler ve backlog öğeleri için gerçek Issue'lar | `gh issue list` | Failed | Yalnızca #3 (QA) ve #5 (DevOps) var; diğer teslimler ve PB Issue'ları yok | Mert |
| QA-17 | Backlog — alan bütünlüğü | `docs/Initial_Backlog_Draft.md` @ `26fc3f4` | Her öğede epic, story, kabul kriteri, öncelik, puan, bağımlılık, sahip | Manuel | Passed | PB-01…PB-07'nin yedisinde tüm alanlar var; PB-03…PB-07 sahibi "To be determined" | Nurefşan |
| QA-18 | Backlog — test edilebilirlik | aynı | Kabul kriterleri ölçülebilir; olumlu ve olumsuz koşul içeriyor | grep + manuel | Failed | Her öğede olumlu ve olumsuz koşul var; PB-07 boş durum mesajı artık somut. PB-02 #4 ve PB-05 #5'te "appropriate response" ölçülebilir değil. Bulgu F-06 | Nurefşan |
| QA-19 | Backlog — onay | aynı, §10 | PO onayı, ekip tahmini, gerçek atama | Manuel | Pending | Onay, tahmin ve atamalar `[TODO]` | Nurefşan |
| QA-20 | Teslim checklist'i | `docs/Sprint1_Submission_Checklist.md` @ `78febb9` | Güncel durum, altı teslim başlığıyla uyum | Manuel | Failed | Bulgu F-07 | Mert |
| QA-21 | Release / tag | GitHub (canlı) | İncelenmiş commit'e bağlı Sprint 1 tag'i | `gh api` | Pending | Tag ve release yok; teslimden önce beklenen | Barış |
| QA-23 | Gereksinim belgelerinin entegrasyonu | `docs/nurefsan-sprint1-requirements` @ `243195e` | Belgeler Issue'ya bağlı PR ile onaylı hedefe gidiyor; aynı dosyanın ikinci sürümü oluşmuyor | `git merge-tree` + `gh` | Failed | PR #7 hedefi `docs/sprint1-team-guides` yapıldı; ancak GitHub PR'ı çakışmalı (`CONFLICTING`) gösteriyor: `Initial_Backlog_Draft.md` hedefteki TR sürümle add/add çakışıyor. PR Issue'ya bağlı değil. Bulgu F-14 | Nurefşan, Mert |
| QA-25 | Vision/Boundary tek belge | `docs/System_Vision_and_Boundary.md` @ `243195e` (PR #7) ve @ `e522c95` (PR #8) | Teslimin tek, birleşik sürümü var | `git merge-tree` | Failed | PR #7'de birleşik belge oluşturuldu; ancak PR #8 eski Boundary-only dosyayı hâlâ içeriyor, iki branch aynı dosyada add/add çakışıyor. Bulgu F-20 | Arda, Nurefşan |
| QA-26 | Commit kimliği | `e522c95` | Commit yazarın ekipteki GitHub hesabına bağlı | `gh api` | Failed | Commit `ardaberkkara@icloud.com` ile atılmış ve `ardaberk00` hesabına bağlı; PR'ı açan ve collaborator olan hesap `ardaberkkara1` (birincil e-posta okul adresi). Bulgu F-22 | Arda |
| QA-24 | Repository kurulum belgesi | `docs/Repository_Setup.md` @ `81a66a9` | Erişim matrisi, clone/branch adımları, doğrulama adımları, eksikler ve kanıt tablosu; geçerli bağlantılar | Manuel + `git cat-file` + `git diff --check` | Passed | 7 bölüm mevcut; 2 göreli bağlantı geçerli; `diff --check` temiz. Güncel olmayan alanlar bulgu F-17'de | Barış |

Özet: 26 kontrolden 11 `Passed`, 11 `Failed`, 4 `Pending`.

## 4. Bulgular

| ID | Öncelik | Bulgu | Önerilen düzeltme | Sahip | Durum |
| --- | --- | --- | --- | --- | --- |
| F-01 | P1 | System Boundary ve `api/openapi.yaml` yoktu. | — | Arda | Kapatıldı (`e522c95`, PR #8); içerik bulguları F-18…F-22 |
| F-02 | — | İlk raporda üyelerin yazma yetkisi olmadığı yazılmıştı. Bu, kontrolün yanlış GitHub hesabıyla yapılmasından kaynaklanan **hatalı bir bulguydu**; altı üyenin de yetkisi var. | — | Ahmet | Kapatıldı (geri çekildi) |
| F-03 | P1 | `develop` yok, branch protection yok. Yazılı Git-Flow kuralları uygulanmıyor. Repository `mert494` kişisel hesabında olduğu için bu ayarları yalnızca Mert (admin) yapabilir; Barış'ın Settings erişimi yok. | Mert `develop`'ı oluşturmalı ve `main`/`develop` için PR zorunluluğu + 1 onay ayarlamalı; Barış kuralları önerir ve kanıtı `Repository_Setup.md`'ye ekler | Mert, Barış | Açık |
| F-04 | P2 | Teslimler ve PB-01…PB-07 için Issue yok (yalnızca #3). | Teslimler ve backlog öğeleri için Issue açılmalı | Mert | Açık |
| F-05 | P2 | PB-07: "anlaşılır boş durum" ölçülebilir değildi. | — | Nurefşan | Kapatıldı (`26fc3f4`: "No published grades are available." mesajı tanımlandı) |
| F-06 | P2 | PB-02 #4 ve PB-05 #5: "appropriate response / appropriate error response" ölçülebilir değil. PB-05'in uygunluk koşulları açık karar olarak listelenmiş (iyileşme), ancak henüz karara bağlanmamış. | Beklenen yanıt somut yazılmalı (ör. yetki yetersizliğinde 403, koşul sağlanmadığında 409/422 ve hata kodu); OpenAPI ile birlikte netleştirilmeli | Nurefşan, Arda | Kısmen çözüldü |
| F-07 | P3 | Checklist "Beş resmî teslim" diyor; Teams ödevinde altı başlık var. "Bu hazırlık commit edilmedi" satırı güncel değil. | Altı başlığa göre güncellenmeli; commit linkleri eklenmeli | Mert | Açık |
| F-08 | P3 | Backlog'da tüm önerilen sahipler Arda idi. | — | Nurefşan, Mert | Kapatıldı (`26fc3f4`: PB-03…PB-07 "To be determined"; dağılım ekip kararı) |
| F-09 | P3 | RACI'de Mert 5 satırda A, 11 satırda R; diğer üyelerde A sayısı 1–4. Hata değil, iş yükü dengesi için bilgi. | Ekip RACI onayında değerlendirmeli | Azra | Açık (bilgi) |
| F-10 | P2 | Proposal'da problem tanımı için kanıt yok; ödev "problem statement and supporting evidence" istiyor. | En az bir kanıt eklenmeli: mevcut üniversite ÖBS'si üzerinde gözlem, öğrencilerle kısa anket veya kaynak gösterilen literatür. Yapılmamış anket yazılmamalı | Nurefşan | Yeni |
| F-11 | P2 | Rol adları belgeler arasında farklı. Proposal: Students, Academic Staff, Student Affairs Personnel, University Management. Backlog: "user", "system administrator", "instructor", "authorized administrator". Birleşik Vision §2.1 dört rol öneriyor (Student, Instructor, Administrator, Student Affairs Staff) ancak paydaşlarla eşlemesi `[TODO]`. | Rol listesi onaylanıp Proposal ve backlog aynı adlarla güncellenmeli; OpenAPI güvenlik şeması bu listeye dayanmalı | Nurefşan, Arda | Kısmen (rol listesi önerildi) |
| F-12 | P3 | Proposal §4 / Vision §4'teki "University Management accessing academic information" ihtiyacının backlog karşılığı yok. | Ya bir PB öğesi eklenmeli ya da bu ihtiyaç kapsam dışı olarak belirtilmeli | Nurefşan | Yeni |
| F-13 | P3 | Lisans gerekçesi genel: MIT'in ne olduğu açıklanmış, bu proje için neden seçildiği yazılmamış. | Projeye özgü 1–2 cümle (ör. ders projesi, açık paylaşım, bağımlılık uyumu) ve ekip kararı eklenmeli | Nurefşan, Arda | Yeni |
| F-14 | P2 | Gereksinim branch'i için Issue yok. PR #7'nin hedefi `docs/sprint1-team-guides` yapıldı; bu nedenle `docs/Initial_Backlog_Draft.md` hedefteki TR sürümle (Mert) çakışıyor ve PR şu an merge edilemiyor. | Hangi sürümün geçerli olduğuna karar verilmeli; çakışma PR #7 branch'inde dosya sahipleriyle çözülmeli ve PR bir Issue'ya bağlanmalı | Nurefşan, Mert | Kısmen (hedef düzeldi; çakışma açık) |
| F-15 | P2 | PR #4 `docs/sprint1-team-guides` → `main`; Mert'in `78febb9` ve `2987dc0` commit'lerini de içeriyor, PR #1'i ve `develop`'ı atlıyor. Commit mesajı "update RACI" diyor ama RACI dosyaları değişmemiş. | PR #4 kapatılmalı veya hedefi `develop` açılınca oraya çevrilmeli; commit/PR açıklaması gerçek değişikliğe göre düzeltilmeli | Azra, Mert | Kısmen (PR #7 hedefi düzeldi; PR #4 hâlâ `main`) |
| F-16 | P3 | PB-05, PB-06, PB-07 user story'lerinde "so that" (fayda) kısmı yok. | Fayda cümlesi eklenmeli | Nurefşan | Yeni |
| F-18 | P2 | OpenAPI'de güvenlik şeması, `security` ve `servers` yok; `info.license` yok. PB-01/PB-02 kimlik doğrulama ve yetki istediği için sözleşme şu an tüm operasyonları güvenliksiz gösteriyor (dosyada bunun kasıtlı `[TODO]` olduğu belirtilmiş). | Taslak bir `securitySchemes` (ör. bearer) ve kök `security` eklenmeli; `servers` için yer tutucu (ör. `http://localhost:8080`) ve `license: MIT` eklenmeli | Arda | Yeni |
| F-19 | P3 | OpenAPI'de hiç `example` ve `tags` yok; `Student`, `Course`, `Registration`, `Grade` şemaları neredeyse alansız. | Ana operasyonlara en az bir sahte örnek eklenmeli; alanlar Nurefşan'ın veri kararlarıyla birlikte genişletilmeli | Arda, Nurefşan | Yeni |
| F-20 | P1 | `docs/System_Vision_and_Boundary.md` iki branch'te ayrı ayrı oluşturulmuştu. `243195e` ile PR #7'de birleşik belge var; ancak PR #8 eski dosyayı hâlâ içeriyor ve iki PR aynı dosyada çakışıyor. | Arda `docs/System_Vision_and_Boundary.md`'yi PR #8'den çıkarmalı (PR #8 yalnızca `api/openapi.yaml` kalmalı); Boundary düzeltmeleri birleşik belgeye yapılmalı | Arda, Nurefşan | Kısmen (birleşik belge var) |
| F-21 | P2 | Boundary bölümünde dış sistemler, arayüzler ve rol izinleri tanımsız ("onaylı dış sistem yok"). Birleşik belgede aktör ↔ SIS etkileşimleri ve beş kapsam dışı madde eklendi. | Dış sistem olmadığı karar olarak yazılmalı veya adayları listelenmeli; basit bir bağlam tablosu/diyagramı eklenmeli; rol izinleri F-11 ile netleştirilmeli | Arda | Kısmen (etkileşimler ve kapsam dışı eşitlendi) |
| F-22 | P2 | `e522c95` commit'i `ardaberkkara@icloud.com` ile atılmış ve `ardaberk00` hesabına bağlı; `ardaberkkara1` hesabında yalnızca okul e-postası kayıtlı. Katkı ekip hesabında görünmez. | Geçmişi yeniden yazmadan çözüm: iCloud adresi `ardaberk00`'dan kaldırılıp `ardaberkkara1`'e eklenmeli. Sonraki commit'ler için `git config user.email` okul adresi yapılmalı | Arda | Yeni |
| F-17 | P3 | `Repository_Setup.md`'de "İlgili Issue: [TODO]" ve "Bu çalışmanın PR'ı: [TODO]" yazıyor, oysa Issue #5 ve PR #6 mevcut. Erişim matrisinde dört üye `[TODO]`; API ile altı üyenin yetkisi doğrulandı (QA-15). Kanıt tablosunda PR #6/#7 ve Issue #5 eksik. | Issue/PR bağlantıları ve erişim düzeyleri güncellenmeli | Barış | Yeni |

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
| F-10, F-12, F-13, F-16, F-17 | [TODO] | [TODO] | [TODO] |

## 6. Açık riskler ve bekleyen kararlar

- OpenAPI 3.1.0 kullanıldı ancak dosyada "aday, ekip onaysız" olarak işaretli. Ekip farklı bir sürüm veya validator seçerse QA-06…QA-08 tekrarlanır.
- PR hedef branch'i (`develop` / `main`) kararı yok. Geçici hedef `docs/sprint1-team-guides` olarak kullanılıyor (PR #2, #6, #8); PR #4 ve #7 `main`'e gidiyor.
- Açık 6 PR'ın (#1, #2, #4, #6, #7, #8) hiçbirinde review yok; teslime kadar merge sırası belirlenmeli.
- Vision/Boundary belgesinin iki ayrı sürümü (F-20) teslim için kritik; birleştirilmeden tek belge teslim edilemez.
- Belge dili karışık: süreç belgeleri Türkçe, gereksinim belgeleri İngilizce. Teslim dili ekipçe seçilmeli.
- Teslim tarihi, takım numarası ve Teams "Sprint 1 Examples" formatı rapora yansıtılmadı [TODO].
- Bu rapor tek kişi tarafından hazırlandı; bağımsız review (öneri: Mert) bekleniyor.
