# Sprint 1 kalite raporu

Durum: **Ara rapor; bağımsız review bekliyor.** Hazırlayan: Ahmet (Quality Assurance and Test Automation Engineer). İlgili Issue: [TODO]. RACI: S1-13 (A/R), S1-05 / S1-09 (C), S1-14 (R).

Bu rapor yalnızca belge, sözleşme ve repository kanıtı kontrolüdür. Çalışan ürün olmadığından birim, entegrasyon veya E2E testi çalıştırılmamıştır; %50 birim test kapsama hedefi Sprint 3'e aittir ve burada değerlendirilmez. Henüz bulunmayan teslimler `Pending` olarak işaretlenmiştir; dosyası olmayan hiçbir kontrol `Passed` sayılmaz.

## 1. Kapsam ve kaynak sürümleri

| Kaynak | Branch / commit | Not |
| --- | --- | --- |
| Repository | `mert494/student-information-system` | Kontrol tarihi: 2026-11-01 |
| Süreç belgeleri | `docs/sprint1-process` @ `78febb9` | RACI, Git_Workflow, backlog taslağı, checklist, şablonlar |
| Ekip rehberleri | `docs/sprint1-team-guides` @ `2987dc0` | PR [#1](https://github.com/mert494/student-information-system/pull/1), açık |
| `main` | `7072b41` | Yalnızca README, LICENSE, .gitignore |

Sonuç değerleri: `Passed`, `Failed`, `Pending`, `Not applicable (gerekçeli)`.

## 2. Yöntem ve araçlar

| Kontrol türü | Yöntem / araç | Durum |
| --- | --- | --- |
| Belge içeriği | Teslim başlıklarına göre manuel okuma | Uygulandı (mevcut dosyalar) |
| RACI tutarlılığı | Python `csv` ile Markdown tablo ↔ CSV satır karşılaştırması; satır başına A ve R sayımı | Uygulandı |
| Ölçülemeyen ifade taraması | `grep` ile backlog'da "kolay, hızlı, uygun, anlaşılır, düzgün, kullanıcı dostu" araması + manuel okuma | Uygulandı |
| GitHub kanıtı | `gh api` ile branch, protection, tag, release, Issue, PR ve contributor sorgusu | Uygulandı (okuma yetkisiyle) |
| OpenAPI doğrulama | Arda'nın seçeceği sürüm ve validator (öneri: `npx @redocly/cli lint api/openapi.yaml`) | `Pending` — dosya yok; Redocly kurulu değil, kurulum izni [TODO]. Ortamda Node v24.13.1, npx 11.8.0, PyYAML 6.0.3 var |

## 3. Kontrol matrisi

| ID | Teslim | Dosya @ commit | Beklenen kriter | Yöntem | Sonuç | Kanıt / not | Bulgu sahibi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-01 | Project Proposal | `docs/Project_Proposal.md` — yok | Problem ve kanıt, paydaş analizi, çözüm ve beklenen çıktılar, fizibilite/kapsam, varsayım/risk | Manuel | Pending | Dosya hiçbir branch'te yok | Nurefşan |
| QA-02 | Lisans seçimi | `LICENSE` @ `7072b41` | Lisans dosyası + proposal içinde seçim gerekçesi | Manuel | Pending | MIT dosyası mevcut; gerekçe ve ekip kararı yok | Nurefşan, Arda |
| QA-03 | System Vision | `docs/System_Vision_and_Boundary.md` — yok | Amaç, hedef kullanıcılar, sistem sorumlulukları ve temel işlevler | Manuel | Pending | Dosya yok | Nurefşan |
| QA-04 | System Boundary | aynı dosya — yok | Sistem bağlamı ve dış etkileşimler, kapsam içi/dışı, kısıt ve varsayımlar | Manuel | Pending | Dosya yok | Arda |
| QA-05 | Kapsam tutarlılığı | Proposal ↔ Vision/Boundary ↔ backlog | Backlog'daki iş boundary dışında kalmamalı | Çapraz okuma | Pending | QA-01, QA-03, QA-04'e bağlı | Nurefşan, Arda |
| QA-06 | OpenAPI — sözdizimi | `api/openapi.yaml` — yok | YAML ayrıştırılır; seçilen OpenAPI sürümüne uygun | Validator | Pending | Dosya yok; validator seçimi [TODO] | Arda |
| QA-07 | OpenAPI — içerik | aynı dosya — yok | Path/HTTP operasyonları, `$ref` çözülür, request/response şemaları, operationId benzersiz, path parametreleri tanımlı, başarı + hata (400/401/403/404) yanıtları | Validator + manuel | Pending | Dosya yok | Arda |
| QA-08 | OpenAPI ↔ backlog | YAML ↔ `docs/Initial_Backlog_Draft.md` | PB-01…PB-07'nin yetki/hata senaryoları sözleşmede karşılık bulur | Çapraz okuma | Pending | QA-06'ya bağlı | Arda, Nurefşan |
| QA-09 | RACI — MD ↔ CSV | `docs/RACI_Matrix.md`, `.csv` @ `78febb9` | 16 satırın kimlik ve hücreleri aynı | Python karşılaştırma | Passed | 16/16 satır birebir aynı; fark yok | Azra |
| QA-10 | RACI — A/R kuralı | aynı | Her satırda tam bir A, en az bir R; yalnızca R/A/C/I, A/R değerleri | Python sayım | Passed | 16 satırın hepsi kurala uyuyor | Azra |
| QA-11 | RACI — ekip kapsamı | aynı | Altı üyenin tamamı ve resmî rolleri yer alıyor | Manuel | Passed | Altı üye ve roller tabloda var | Azra |
| QA-12 | RACI — onay | aynı | Ekip onay tarihi / karar kaydı | Manuel | Pending | Onay tarihi `[TODO]`; Mert–Azra ayrımı onaysız | Azra, Mert |
| QA-13 | Git-Flow kuralları (yazılı) | `docs/Git_Workflow.md` @ `78febb9` | `main` / `develop` / `feature` dal modeli, commit biçimi, PR, review, merge, protection kuralları | Manuel | Passed | Tüm başlıklar mevcut; belge "onaysız taslak" olarak işaretli | Mert |
| QA-14 | Git-Flow — uygulama | GitHub (canlı) | `develop` var; `main`/`develop` korumalı; PR'lar `develop`'a gidiyor | `gh api` | Failed | `develop` yok; `main` dahil hiçbir branch korumalı değil; PR #1 hedefi `docs/sprint1-process` | Barış, Mert |
| QA-15 | GitHub erişimi / katkı | GitHub (canlı) | Altı üyenin yazma yetkisi; her üyenin kendi commit/Issue/PR'ı | `gh api` | Failed | Tek contributor: `mert494`; Ahmet hesabının yazma yetkisi yok (`push: false`) | Barış |
| QA-16 | Issues / Projects | GitHub (canlı) | Teslimler ve backlog öğeleri için gerçek Issue'lar | `gh issue list` | Failed | Repository'de hiç Issue yok | Mert |
| QA-17 | Backlog — alan bütünlüğü | `docs/Initial_Backlog_Draft.md` @ `78febb9` | Her öğede epic, story, kabul kriteri, öncelik, puan, bağımlılık, sahip | Manuel | Passed | PB-01…PB-07'nin yedisinde de tüm alanlar var | Nurefşan |
| QA-18 | Backlog — test edilebilirlik | aynı | Kabul kriterleri ölçülebilir; olumlu ve olumsuz koşul içeriyor | grep + manuel | Failed | Bulgu F-05, F-06 | Nurefşan |
| QA-19 | Backlog — onay | aynı | PO onayı, ekip tahmini, gerçek atama | Manuel | Pending | Tüm öğeler "örnek"; onay `[TODO]` | Nurefşan |
| QA-20 | Teslim checklist'i | `docs/Sprint1_Submission_Checklist.md` @ `78febb9` | Güncel durum, altı teslim başlığıyla uyum | Manuel | Failed | Bulgu F-07 | Mert |
| QA-21 | Release / tag | GitHub (canlı) | İncelenmiş commit'e bağlı Sprint 1 tag'i | `gh api` | Pending | Tag ve release yok; teslimden önce beklenen | Barış |

Özet: 21 kontrolden 5 `Passed`, 5 `Failed`, 11 `Pending`.

## 4. Bulgular

| ID | Öncelik | Bulgu | Önerilen düzeltme | Sahip | Kontrol |
| --- | --- | --- | --- | --- | --- |
| F-01 | P1 | Proposal, Vision/Boundary ve `openapi.yaml` hiçbir branch'te yok. Sprint 1'in altı teslim başlığından üçü içeriksiz. | Dosyaların taslak hâli PR olarak açılmalı | Nurefşan, Arda | QA-01…QA-08 |
| F-02 | P1 | Üyelerin repository'ye yazma yetkisi yok; tek contributor `mert494`. Rubrikteki bireysel katkı (15 puan) kanıtlanamaz. | Altı üye collaborator (Write) olarak eklenmeli veya organization'a taşınmalı | Barış, Mert | QA-15 |
| F-03 | P1 | `develop` yok, branch protection yok. Yazılı Git-Flow kuralları uygulanmıyor. | `develop` oluşturulmalı; `main` ve `develop` için PR zorunluluğu + 1 onay ayarlanmalı | Barış | QA-14 |
| F-04 | P2 | Repository'de hiç Issue yok; PB ve S1 kimlikleri gerçek Issue'lara bağlı değil. | Teslimler ve PB-01…PB-07 için Issue açılmalı | Mert | QA-16 |
| F-05 | P2 | PB-07: "veri yoksa **anlaşılır** boş durum gösterilir" ölçülebilir değil. | Gösterilecek mesaj veya davranış somut yazılmalı (ör. "Yayımlanmış not yok" metni) | Nurefşan | QA-18 |
| F-06 | P2 | PB-05: "**Uygun** öğrenci" ve "uygun dönem" tanımsız; uygunluk koşulu (kayıt durumu, önkoşul, kontenjan) belirtilmemiş. | Uygunluk kuralları kabul kriterine yazılmalı veya PO kararına bağlanmalı | Nurefşan | QA-18 |
| F-07 | P3 | Checklist "Beş resmî teslim" diyor; Teams ödevinde altı başlık var. "Bu hazırlık commit edilmedi" satırı artık güncel değil (`78febb9` mevcut). | Altı başlığa göre güncellenmeli; commit linki eklenmeli | Mert | QA-20 |
| F-08 | P3 | Backlog'da PB-01…PB-07'nin hepsinde önerilen sahip Arda. Uygulama yükü tek kişide toplanıyor; bireysel katkı dağılımı için risk. | Uygulayıcılar story bazında ekipçe dağıtılmalı | Nurefşan, Mert | QA-19 |
| F-09 | P3 | RACI'de Mert 5 satırda A, 11 satırda R; diğer üyelerde A sayısı 1–4. Hata değil, iş yükü dengesi için bilgi. | Ekip RACI onayında değerlendirmeli | Azra | QA-12 |

Bulgular için gerçek Issue açılmadı; açılması Mert ile koordineli ve onaya bağlıdır. Issue taslağı için `.github/ISSUE_TEMPLATE/documentation.md` kullanılacak.

## 5. Yeniden kontroller

| Bulgu | Düzeltme PR / commit | Yeniden kontrol tarihi | Sonuç |
| --- | --- | --- | --- |
| F-01…F-09 | [TODO] | [TODO] | [TODO] |

## 6. Açık riskler ve bekleyen kararlar

- OpenAPI sürümü (3.0 / 3.1) ve validator Arda tarafından seçilmedi; QA-06 ve QA-07 buna bağlı.
- PR hedef branch'i (`develop` / `main`) kararı yok; bu rapor dahil hiçbir PR hedefi netleşmedi.
- Teslim tarihi, takım numarası ve Teams "Sprint 1 Examples" formatı rapora yansıtılmadı [TODO].
- Bu rapor tek kişi tarafından hazırlandı; bağımsız review (öneri: Mert) bekleniyor.
