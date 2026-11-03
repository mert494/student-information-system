# Sprint 1 eksikler ve görev listesi

Durum: **QA kontrolüne dayalı görev listesi; 2026-11-03 (öğleden sonra) itibarıyla günceldir.** Hazırlayan: Ahmet (QA). Kaynak: [Sprint1_Quality_Report.md](Sprint1_Quality_Report.md); `F-xx` ve `QA-xx` kimlikleri o rapordaki bulgu ve kontrollerdir. İlgili Issue: [#3](https://github.com/mert494/student-information-system/issues/3).

Teslim: **5 Kasım 2026, 23:59**. Önerilen ara hedef: düzeltmeler ve review'lar **3 Kasım akşamı**, merge ve tag **4 Kasım**.

Her üye kendi bölümündeki maddeleri tamamladıkça `[ ]` kutusunu `[x]` yapıp kendi PR'ında işaretler. Bir madde yapılmayacaksa silmeyin; yanına gerekçesini yazın. QA, işaretlenen maddeleri yeniden kontrol edip rapora işler.

## Sprint 1 teslim başlıklarına göre durum

| # | Teslim başlığı (Teams) | Sahip | Belge / PR | Durum | Açık bulgular |
| --- | --- | --- | --- | --- | --- |
| 1 | Project Proposal | Nurefşan | `docs/Project_Proposal.md`, PR [#7](https://github.com/mert494/student-information-system/pull/7) | Var; kanıt ve lisans gerekçesi eksik | F-10, F-13 |
| 2 | System Vision and Boundary | Vision: Nurefşan, Boundary: Arda | `docs/System_Vision_and_Boundary.md`, PR #7 ve [#8](https://github.com/mert494/student-information-system/pull/8) | PR #7'de birleşik belge var; PR #8 eski dosyayı hâlâ içeriyor; dış sistemler `[TODO]` | F-11, F-12, F-20, F-21 |
| 3 | OpenAPI Draft | Arda | `api/openapi.yaml`, PR #8 | Var; yapı geçerli, güvenlik/servers/license eksik | F-18, F-19 |
| 4 | Team Roles and RACI | Azra | `docs/RACI_Matrix.md` / `.csv`, PR [#4](https://github.com/mert494/student-information-system/pull/4) | Teknik olarak doğru; ekip onayı yok | F-09, F-15 |
| 5 | GitHub Repository and Git-Flow | Barış, Mert | `docs/Git_Workflow.md`, `docs/Repository_Setup.md`, PR [#6](https://github.com/mert494/student-information-system/pull/6) | Kurallar yazılı; `develop`, koruma, Issue ve tag yok | F-03, F-04, F-14, F-15, F-17 |
| 6 | Initial Product Backlog | Nurefşan | `docs/Initial_Backlog_Draft.md`, PR #7 | Var; PR #7 hedefteki TR sürümle çakışıyor, iki kriter ölçülemiyor | F-06, F-14, F-16 |
| — | Submission (takım bilgisi, linkler, tag) | Mert | `docs/Sprint1_Submission_Checklist.md` | Güncel değil | F-07 |

## Herkes için ortak görevler

- [ ] Kendi PR'ın yazarı dışında en az bir kişiden review al; sana atanan PR'ları review et.
- [ ] Commit'lerin ekipteki GitHub hesabına bağlı olsun: `git config user.email` hesabında kayıtlı bir e-posta olmalı.
- [ ] Kendi teslimine ait gerçek Issue, PR ve commit linklerini Mert'e ilet (checklist'teki bireysel katkı tablosu için).
- [ ] Kendi belgende kalan `[TODO]`'ları ya doldur ya da "karar bekliyor" diye sahibini yaz.
- [ ] PR hedefini ekipçe seçilen hedefe çevir (aşağıdaki merge önerisine bakın).

## Nurefşan — Product Owner and Requirements Engineer

- [ ] **F-10** Proposal §2'ye problem için en az bir kanıt ekle: mevcut ÖBS üzerinde gözlem, öğrencilerle kısa anket veya kaynak gösterilen literatür. Yapılmamış bir anketi yapılmış gibi yazma.
- [ ] **F-11** Vision §2.1'deki dört rolü onaylatıp Proposal ve backlog'da aynı adları kullan ("Administrator" ile "University Management" ilişkisi?). Listeyi Arda'ya OpenAPI güvenlik şeması için ilet.
- [x] **F-20** Arda ile `System_Vision_and_Boundary.md` dosyasını tek dosyada birleştirin: Vision bölümü senin sürümünden. (`243195e`)
- [x] PR #7'nin hedefini ortak hedefe (`docs/sprint1-team-guides`) çevir.
- [ ] **F-14** PR #7 şu an çakışmalı: backlog'un hangi sürümünün kalacağına Mert ile karar ver (seninki daha güncel), çakışmayı PR #7 branch'inde çöz ve PR'ı bir Issue'ya bağla.
- [ ] **F-06** PB-02 #4 ve PB-05 #5'teki "appropriate response" yerine somut yanıt yaz (ör. yetki yetersizse 403, koşul sağlanmazsa 409/422 ve hata kodu).
- [ ] **F-12** "University Management" ihtiyacı için ya bir PB maddesi ekle ya da kapsam dışı olarak yaz.
- [ ] **F-13** Lisans bölümüne MIT'in bu proje için neden seçildiğini 1–2 cümleyle ekle.
- [ ] **F-16** PB-05, PB-06 ve PB-07 user story'lerine "so that ..." fayda kısmını ekle.
- [ ] **QA-19** Backlog'un PO onayını ve ekip tahminlerini kaydet.

## Arda — Lead Software Architect and Technical Lead

- [ ] **F-20** Nurefşan birleşik belgeyi PR #7'de oluşturdu. `docs/System_Vision_and_Boundary.md`'yi PR #8'den çıkar (PR #8'de yalnızca `api/openapi.yaml` kalsın); Boundary düzeltmelerini birleşik belgeye yap.
- [ ] **F-21** Birleşik belgede §4.4'ü tamamla: dış sistem olmadığını karar olarak yaz veya adayları listele, basit bir bağlam tablosu/diyagramı ekle. (Kapsam dışı listesi artık eşit.)
- [ ] **F-18** `openapi.yaml`'a taslak bir `securitySchemes` (ör. bearer) ve kök `security`, `servers` için yer tutucu (ör. `http://localhost:8080`) ve `info.license: MIT` ekle.
- [ ] **F-19** Ana operasyonlara en az birer sahte `example` ve `tags` ekle; `Student`, `Course`, `Registration`, `Grade` şemalarına temel alanları ekle.
- [ ] **F-22** Commit'in `ardaberk00` hesabına gitmiş. iCloud adresini `ardaberk00`'dan kaldırıp `ardaberkkara1`'e ekle; sonraki commit'ler için `git config user.email` okul adresin olsun.
- [ ] Düzeltmelerden sonra `npx @redocly/cli lint api/openapi.yaml` çalıştırıp sonucu PR'a yaz (QA ayrıca tekrar kontrol eder).

## Mert — Scrum Master and Agile Process Coach

- [ ] **F-03** `develop` branch'ini oluştur; `main` ve `develop` için PR zorunluluğu ve en az 1 onay kuralını aç (yalnızca repository sahibi yapabilir).
- [ ] **F-04** Her teslim başlığı ve PB-01…PB-07 için Issue aç; ilgili PR'lara bağla.
- [ ] **F-07** Checklist'i altı teslim başlığına göre güncelle; "commit edilmedi" satırını gerçek commit linkiyle değiştir; bireysel katkı tablosunu doldur.
- [ ] **F-14** Nurefşan ile backlog'un geçerli sürümüne karar ver.
- [ ] PR'lara reviewer ata ve merge sırasını ekibe duyur (aşağıdaki öneriye bakın).
- [ ] PR [#2](https://github.com/mert494/student-information-system/pull/2)'yi (QA raporu) review et.
- [ ] Final teslimi Teams'te yap: takım numarası, proje adı, üyeler, repository URL'si, OpenAPI YAML, Issue/PR/commit linkleri ve Sprint 1 tag'i.

## Azra — Scrum Master and Agile Process Coach

- [ ] **F-15** PR #4'ün hedefi `main`; Mert'in commit'lerini de içeriyor. Aşağıdaki merge önerisine göre PR #4'ü kapatmayı ya da hedefini değiştirmeyi Mert ile netleştir.
- [ ] **F-15** Commit/PR açıklamasını gerçek değişikliğe göre düzelt: "update RACI" yazıyor ama RACI dosyaları değişmedi.
- [ ] **QA-12** RACI'nin ekip onayını, tarihini ve Mert–Azra iş bölümü kararını kaydet.
- [ ] `Sprint1_Process_Records.md`'deki "Role Assignment" tablosunu ve toplantı/karar kayıtlarını gerçekleşmiş olanlarla doldur. Yapılmamış toplantı yazma.
- [ ] **F-09** RACI onayında Mert'in A/R yükünü (5 A, 11 R) ekiple değerlendir.

## Barış — DevOps and CI/CD Infrastructure Engineer

- [ ] **F-17** `Repository_Setup.md`'de Issue'yu (#5) ve PR'ı (#6) bağla; erişim tablosunu güncelle. Altı üyenin de Write yetkisi var, Mert admin.
- [ ] **F-03** Mert ayarları açtıktan sonra branch kuralının kanıtını (ekran görüntüsü veya ayar özeti) belgeye ekle.
- [ ] **QA-21** Tüm PR'lar merge edildikten sonra Mert ile Sprint 1 tag'ini ve release'i oluştur (öneri: `sprint-1`) ve linki checklist'e ekle.

## Ahmet — Quality Assurance and Test Automation Engineer

- [x] Altı teslim başlığı için kontrol matrisini hazırla (`Sprint1_Quality_Report.md`, 26 kontrol).
- [x] OpenAPI'yi Redocly ile doğrula ve backlog ile eşleştir (QA-06…QA-08).
- [x] Bulguları sahipleriyle birlikte listele (bu belge).
- [ ] Düzeltmeler geldikçe ilgili kontrolleri yeniden çalıştır ve raporun "Yeniden kontroller" tablosunu doldur.
- [ ] Merge sonrası son durumu kontrol et: tek Vision/Boundary belgesi, geçerli OpenAPI, tag doğru commit'te.
- [ ] Kendi Issue/PR/commit linklerini Mert'e ilet.

## Önerilen merge sırası

Karar Mert'indir; bu bir öneridir.

1. Mert PR #1'i merge eder. PR #1'in kaynak branch'i Azra'nın `79e3d40` commit'ini de içerdiği için PR #4'ün içeriği de bununla gelir; PR #4 kapatılabilir.
2. Mert `docs/sprint1-process`'ten `develop`'ı oluşturur ve branch kurallarını açar.
3. PR #2, #6, #7 ve #8'in hedefi `develop` yapılır.
4. Sırasıyla PR #6 (Barış), PR #8 (Arda; Vision/Boundary birleştirmesiyle), PR #7 (Nurefşan; backlog çakışması çözülerek) review edilip merge edilir.
5. QA son kontrolü yapar; PR #2 en son merge edilir.
6. `develop` → `main` PR'ı açılır, review sonrası merge edilir ve `main` üzerindeki commit'e Sprint 1 tag'i atılır.
