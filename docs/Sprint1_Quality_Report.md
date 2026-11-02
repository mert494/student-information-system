# Sprint 1 kalite raporu

Durum: **Ara rapor; bağımsız review bekliyor.** Hazırlayan: Ahmet (Quality Assurance and Test Automation Engineer). İlgili Issue: [#3](https://github.com/mert494/student-information-system/issues/3). RACI: S1-13 (A/R), S1-05 / S1-09 (C), S1-14 (R).

Bu rapor yalnızca belge, sözleşme ve repository kanıtı kontrolüdür. Çalışan ürün olmadığından birim, entegrasyon veya E2E testi çalıştırılmamıştır; %50 birim test kapsama hedefi Sprint 3'e aittir ve burada değerlendirilmez. Henüz bulunmayan teslimler `Pending` olarak işaretlenmiştir; dosyası olmayan hiçbir kontrol `Passed` sayılmaz.

## 1. Kapsam ve kaynak sürümleri

| Kaynak | Branch / commit | Not |
| --- | --- | --- |
| Repository | `mert494/student-information-system` | İlk kontrol: 2026-11-01; yeniden kontroller: 2026-11-02 (iki tur) |
| Süreç belgeleri | `docs/sprint1-process` @ `78febb9` | RACI, Git_Workflow, backlog taslağı (TR), checklist, şablonlar |
| Ekip rehberleri + süreç kayıtları | `docs/sprint1-team-guides` @ `79e3d40` | PR [#1](https://github.com/mert494/student-information-system/pull/1) ve [#4](https://github.com/mert494/student-information-system/pull/4), açık |
| Gereksinim belgeleri | `docs/nurefsan-sprint1-requirements` @ `26fc3f4` | Proposal, Vision/Boundary, backlog (EN); PR [#7](https://github.com/mert494/student-information-system/pull/7) → `main` |
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
| OpenAPI doğrulama | Redocly CLI 2.72.1 (`npx redocly lint api/openapi.yaml`, varsayılan `recommended` kuralları); Node v24.13.1. Kesin OpenAPI sürümü Arda'nın seçimine bağlı | Araç hazır; `api/openapi.yaml` olmadığı için `Pending`. Araç, örnek bir 3.1 dosyasında hatasız sonuç verdi; tanımsız path parametresi ve çözülmeyen `$ref` içeren bozuk örnekte 3 hata yakaladı (repository'ye eklenmedi) |

## 3. Kontrol matrisi

| ID | Teslim | Dosya @ commit | Beklenen kriter | Yöntem | Sonuç | Kanıt / not | Bulgu sahibi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-01 | Project Proposal — başlıklar | `docs/Project_Proposal.md` @ `26fc3f4` | Problem, paydaş analizi, çözüm ve beklenen çıktılar, fizibilite/kapsam, varsayım/risk, lisans | Manuel | Passed | 12 bölüm; ödevdeki tüm başlıklar karşılanıyor | Nurefşan |
| QA-22 | Project Proposal — kanıt | aynı | Problem tanımı destekleyici kanıta dayanıyor | Manuel | Failed | Bölüm 2 problemlerin doğrulanmamış varsayım olduğunu açıkça belirtiyor; kaynak, anket veya gözlem yok. Bulgu F-10 | Nurefşan |
| QA-02 | Lisans seçimi | `LICENSE` @ `7072b41`, Proposal §10 | Lisans dosyası + projeye özgü seçim gerekçesi + ekip kararı | Manuel | Pending | MIT dosyası ve genel açıklama var; projeye özgü gerekçe ve ekip kararı yok. Bulgu F-13 | Nurefşan, Arda |
| QA-03 | System Vision | `docs/System_Vision_and_Boundary.md` @ `26fc3f4` | Amaç, hedef kullanıcılar, sistem sorumlulukları ve temel işlevler | Manuel | Passed | §1–3 mevcut; 4 kullanıcı grubu ve 6 işlev tanımlı | Nurefşan |
| QA-04 | System Boundary | aynı, §4–5 | Sistem bağlamı ve dış etkileşimler, kapsam içi/dışı, kısıt ve varsayımlar | Manuel | Pending | Kapsam içi/dışı ve kısıtlar var; dış aktörler, dış sistemler ve arayüzler `[TODO – Arda]` | Arda |
| QA-05 | Kapsam tutarlılığı | Proposal ↔ Vision/Boundary ↔ backlog @ `26fc3f4` | Roller ve özellikler üç belgede aynı; backlog'daki iş boundary dışında kalmıyor | Çapraz okuma | Failed | Kapsam dışı listeleri iki belgede aynı ve backlog'da kapsam dışı iş yok; ancak rol adları uyuşmuyor ve bir özelliğin backlog karşılığı yok. Bulgu F-11, F-12 | Nurefşan, Arda |
| QA-06 | OpenAPI — sözdizimi | `api/openapi.yaml` — yok | YAML ayrıştırılır; seçilen OpenAPI sürümüne uygun | Redocly lint | Pending | Dosya yok; araç hazır, sürüm seçimi [TODO] | Arda |
| QA-07 | OpenAPI — içerik | aynı dosya — yok | Path/HTTP operasyonları, `$ref` çözülür, request/response şemaları, operationId benzersiz, path parametreleri tanımlı, başarı + hata (400/401/403/404) yanıtları | Validator + manuel | Pending | Dosya yok | Arda |
| QA-08 | OpenAPI ↔ backlog | YAML ↔ backlog | PB-01…PB-07'nin yetki/hata senaryoları sözleşmede karşılık bulur | Çapraz okuma | Pending | QA-06'ya bağlı | Arda, Nurefşan |
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
| QA-23 | Gereksinim belgelerinin entegrasyonu | `docs/nurefsan-sprint1-requirements` @ `26fc3f4` | Belgeler Issue'ya bağlı PR ile onaylı hedefe gidiyor; aynı dosyanın ikinci sürümü oluşmuyor | `git` + `gh` | Failed | PR #7 açıldı ancak `main`'i hedefliyor ve Issue'ya bağlı değil; `Initial_Backlog_Draft.md` `docs/sprint1-process`'teki TR sürümle aynı yolda. `main`'de bu dosya henüz olmadığı için GitHub şu an çakışma göstermiyor; süreç branch'i `main`'e girince çakışacak. Bulgu F-14 | Nurefşan, Mert |
| QA-24 | Repository kurulum belgesi | `docs/Repository_Setup.md` @ `81a66a9` | Erişim matrisi, clone/branch adımları, doğrulama adımları, eksikler ve kanıt tablosu; geçerli bağlantılar | Manuel + `git cat-file` + `git diff --check` | Passed | 7 bölüm mevcut; 2 göreli bağlantı geçerli; `diff --check` temiz. Güncel olmayan alanlar bulgu F-17'de | Barış |

Özet: 24 kontrolden 9 `Passed`, 7 `Failed`, 8 `Pending`.

## 4. Bulgular

| ID | Öncelik | Bulgu | Önerilen düzeltme | Sahip | Durum |
| --- | --- | --- | --- | --- | --- |
| F-01 | P1 | System Boundary (dış aktörler, dış sistemler, arayüzler) ve `api/openapi.yaml` hâlâ yok. | Arda Boundary bölümünü doldurmalı ve OpenAPI taslağını PR olarak açmalı | Arda | Açık (Proposal ve Vision geldi) |
| F-02 | — | İlk raporda üyelerin yazma yetkisi olmadığı yazılmıştı. Bu, kontrolün yanlış GitHub hesabıyla yapılmasından kaynaklanan **hatalı bir bulguydu**; altı üyenin de yetkisi var. | — | Ahmet | Kapatıldı (geri çekildi) |
| F-03 | P1 | `develop` yok, branch protection yok. Yazılı Git-Flow kuralları uygulanmıyor. Repository `mert494` kişisel hesabında olduğu için bu ayarları yalnızca Mert (admin) yapabilir; Barış'ın Settings erişimi yok. | Mert `develop`'ı oluşturmalı ve `main`/`develop` için PR zorunluluğu + 1 onay ayarlamalı; Barış kuralları önerir ve kanıtı `Repository_Setup.md`'ye ekler | Mert, Barış | Açık |
| F-04 | P2 | Teslimler ve PB-01…PB-07 için Issue yok (yalnızca #3). | Teslimler ve backlog öğeleri için Issue açılmalı | Mert | Açık |
| F-05 | P2 | PB-07: "anlaşılır boş durum" ölçülebilir değildi. | — | Nurefşan | Kapatıldı (`26fc3f4`: "No published grades are available." mesajı tanımlandı) |
| F-06 | P2 | PB-02 #4 ve PB-05 #5: "appropriate response / appropriate error response" ölçülebilir değil. PB-05'in uygunluk koşulları açık karar olarak listelenmiş (iyileşme), ancak henüz karara bağlanmamış. | Beklenen yanıt somut yazılmalı (ör. yetki yetersizliğinde 403, koşul sağlanmadığında 409/422 ve hata kodu); OpenAPI ile birlikte netleştirilmeli | Nurefşan, Arda | Kısmen çözüldü |
| F-07 | P3 | Checklist "Beş resmî teslim" diyor; Teams ödevinde altı başlık var. "Bu hazırlık commit edilmedi" satırı güncel değil. | Altı başlığa göre güncellenmeli; commit linkleri eklenmeli | Mert | Açık |
| F-08 | P3 | Backlog'da tüm önerilen sahipler Arda idi. | — | Nurefşan, Mert | Kapatıldı (`26fc3f4`: PB-03…PB-07 "To be determined"; dağılım ekip kararı) |
| F-09 | P3 | RACI'de Mert 5 satırda A, 11 satırda R; diğer üyelerde A sayısı 1–4. Hata değil, iş yükü dengesi için bilgi. | Ekip RACI onayında değerlendirmeli | Azra | Açık (bilgi) |
| F-10 | P2 | Proposal'da problem tanımı için kanıt yok; ödev "problem statement and supporting evidence" istiyor. | En az bir kanıt eklenmeli: mevcut üniversite ÖBS'si üzerinde gözlem, öğrencilerle kısa anket veya kaynak gösterilen literatür. Yapılmamış anket yazılmamalı | Nurefşan | Yeni |
| F-11 | P2 | Rol adları belgeler arasında farklı. Proposal/Vision: Students, Academic Staff, Student Affairs Personnel, University Management. Backlog: "user", "system administrator", "instructor", "authorized administrator". "Administrator" hangi gruba karşılık geliyor belli değil. | Tek bir rol listesi belirlenip üç belgede aynı adlar kullanılmalı; OpenAPI güvenlik şeması da bu listeye dayanmalı | Nurefşan, Arda | Yeni |
| F-12 | P3 | Proposal §4 / Vision §4'teki "University Management accessing academic information" ihtiyacının backlog karşılığı yok. | Ya bir PB öğesi eklenmeli ya da bu ihtiyaç kapsam dışı olarak belirtilmeli | Nurefşan | Yeni |
| F-13 | P3 | Lisans gerekçesi genel: MIT'in ne olduğu açıklanmış, bu proje için neden seçildiği yazılmamış. | Projeye özgü 1–2 cümle (ör. ders projesi, açık paylaşım, bağımlılık uyumu) ve ekip kararı eklenmeli | Nurefşan, Arda | Yeni |
| F-14 | P2 | Gereksinim branch'i için Issue yok; PR #7 `main`'i hedefliyor; branch `main`'den açılmış. `docs/Initial_Backlog_Draft.md` hem `docs/sprint1-process`'te (TR, Mert) hem bu branch'te (EN, Nurefşan) var; birleşince çakışır ve iki sürüm oluşur. | Hangi sürümün geçerli olduğuna karar verilmeli; PR #7'nin hedefi ortak geçici hedefe (`docs/sprint1-team-guides`) çevrilmeli ve çakışma dosya sahipleriyle çözülmeli | Nurefşan, Mert | Kısmen (PR açıldı) |
| F-15 | P2 | PR #4 `docs/sprint1-team-guides` → `main`; Mert'in `78febb9` ve `2987dc0` commit'lerini de içeriyor, PR #1'i ve `develop`'ı atlıyor. Commit mesajı "update RACI" diyor ama RACI dosyaları değişmemiş. PR #7 de `main`'i hedefliyor; `Repository_Setup.md` §4 ise geçici hedefi `docs/sprint1-team-guides` olarak tanımlıyor, yani PR hedefleri tutarsız. | PR hedefi `develop` açılınca oraya çevrilmeli veya PR #1 ile birleştirme sırası netleştirilmeli; commit/PR açıklaması gerçek değişikliğe göre düzeltilmeli | Azra, Mert | Yeni |
| F-16 | P3 | PB-05, PB-06, PB-07 user story'lerinde "so that" (fayda) kısmı yok. | Fayda cümlesi eklenmeli | Nurefşan | Yeni |
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
| F-10…F-13, F-15…F-17 | [TODO] | [TODO] | [TODO] |

## 6. Açık riskler ve bekleyen kararlar

- OpenAPI sürümü (3.0 / 3.1) Arda tarafından seçilmedi; QA-06 ve QA-07 buna bağlı. Ekip farklı bir validator seçerse kontroller onunla tekrarlanır.
- PR hedef branch'i (`develop` / `main`) kararı yok. Geçici hedef `docs/sprint1-team-guides` olarak kullanılıyor (PR #2, #6); PR #4 ve #7 `main`'e gidiyor.
- Açık 5 PR'ın (#1, #2, #4, #6, #7) hiçbirinde review yok; teslime kadar merge sırası belirlenmeli.
- Arda'dan Boundary bölümü ve `api/openapi.yaml` henüz gelmedi; QA-04, QA-06…QA-08 teslim için kritik.
- Belge dili karışık: süreç belgeleri Türkçe, gereksinim belgeleri İngilizce. Teslim dili ekipçe seçilmeli.
- Teslim tarihi, takım numarası ve Teams "Sprint 1 Examples" formatı rapora yansıtılmadı [TODO].
- Bu rapor tek kişi tarafından hazırlandı; bağımsız review (öneri: Mert) bekleniyor.
