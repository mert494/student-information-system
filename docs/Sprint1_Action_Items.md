# Sprint 1 eksikler ve görev listesi

Durum: **QA kontrolüne dayalı görev listesi; 2026-11-04 (akşam, PR #7, #8, #6, #19 merge'ü ve PR #17 yeniden kontrolü) itibarıyla günceldir.** Hazırlayan: Ahmet (QA). Kaynak: [Sprint1_Quality_Report.md](Sprint1_Quality_Report.md); `F-xx` ve `QA-xx` kimlikleri o rapordaki bulgu ve kontrollerdir. İlgili Issue: [#3](https://github.com/mert494/student-information-system/issues/3).

Teslim: **5 Kasım 2026, 23:59**. Önerilen ara hedef: kalan düzeltmeler ve review'lar **4 Kasım öğlen**, merge, `develop` → `main` ve tag **4 Kasım akşam**; 5 Kasım yedek gün.

Her üyenin Codex'e yapıştıracağı hazır prompt'lar ve çalıştırma sırası: [Sprint1_Codex_Prompts.md](Sprint1_Codex_Prompts.md).

Her üye kendi bölümündeki maddeleri tamamladıkça `[ ]` kutusunu `[x]` yapıp kendi PR'ında işaretler. Bir madde yapılmayacaksa silmeyin; yanına gerekçesini yazın. QA, işaretlenen maddeleri yeniden kontrol edip rapora işler.

## Sprint 1 teslim başlıklarına göre durum

| # | Teslim başlığı (Teams) | Sahip | Belge / PR | Durum | Açık bulgular |
| --- | --- | --- | --- | --- | --- |
| 1 | Project Proposal | Nurefşan | `docs/Project_Proposal.md`, PR [#7](https://github.com/mert494/student-information-system/pull/7) | `develop`'ta (merge `6ad16ce`) | — |
| 2 | System Vision and Boundary | Vision: Nurefşan, Boundary: Arda | `docs/System_Vision_and_Boundary.md`, PR #7 ve PR [#19](https://github.com/mert494/student-information-system/pull/19) | `develop`'ta tek birleşik belge; dış sistem kararı "proposed" | — |
| 3 | OpenAPI Draft | Arda | `api/openapi.yaml`, PR [#8](https://github.com/mert494/student-information-system/pull/8) | `develop`'ta (merge `36c7c8f`); Redocly 0 hata | F-19 (küçük) |
| 4 | Team Roles and RACI | Azra | `docs/RACI_Matrix.md` / `.csv`, `docs/Sprint1_Process_Records.md`, PR [#17](https://github.com/mert494/student-information-system/pull/17) | F-24 düzeltildi (`85eec71`); Mert'in yeniden onayı ve merge bekliyor | — |
| 5 | GitHub Repository and Git-Flow | Barış, Mert | `docs/Git_Workflow.md`, `docs/Repository_Setup.md` (ikisi de `develop`'ta) | `develop` ve ruleset'ler aktif; kurulum belgesi merge edildi (`1b6825b`); `develop` → `main` ve tag yok | QA-21 |
| 6 | Initial Product Backlog | Nurefşan | `docs/Initial_Backlog_Draft.md`, PR #7 | `develop`'ta; küçük tutarsızlıklar; PB Issue'ları yok | F-23, F-04 |
| — | Submission (takım bilgisi, linkler, tag) | Mert | `docs/Sprint1_Submission_Checklist.md` (`develop`'ta) | Güncel; final linkler ve tag bekliyor | — |

## Herkes için ortak görevler

- [x] PR hedefini `develop` yap (tüm açık PR'lar `develop`'u hedefliyor).
- [ ] Kendi PR'ın için yazar dışı en az bir onay al; sana atanan PR'ları review et.
- [ ] Commit'lerin ekipteki GitHub hesabına bağlı olsun: `git config user.email` hesabında kayıtlı bir e-posta olmalı.
- [ ] Kendi teslimine ait gerçek Issue, PR ve commit linklerini Mert'e ilet (checklist'teki bireysel katkı tablosu için).

## Nurefşan — Product Owner and Requirements Engineer

- [x] **F-10** Proposal'a ÖBS ön incelemesi eklendi (`c7e9d79`).
- [x] **F-11** Dört sistem rolü ve paydaş → rol eşlemesi üç belgede aynı (`e0226bb`).
- [x] **F-12** University Management → Administrators; özel işlevler kapsam dışı (`e0226bb`).
- [x] **F-13** MIT gerekçesi eklendi (`1184b26`).
- [x] **F-14** PR #7'deki backlog çakışması çözüldü (`6d92c07`).
- [x] **F-06** Somut yanıtlar: 403 / 409 + hata kodu (`69832d5`, `e0226bb`).
- [x] **F-16** Yedi story'nin hepsinde "so that" var.
- [x] **F-20** Birleşik Vision/Boundary belgesi (`243195e`).
- [ ] **F-23** (isteğe bağlı; PR #7 merge edildiği için `develop`'tan yeni PR ile) PB-05'teki "University Management is responsible for defining the enrollment dates" → "Administrators"; PB-05'e "Proposed Owner" alanı ekle; isteğe bağlı: "Administrators" → "Administrator".
- [x] **F-23** PR #7 açıklamasına "Refs #11, #12, #15" eklendi.
- [ ] **F-25** Kişisel Gmail adresini `nsankcc` hesabından kaldırıp `nsnkcc` hesabına ekle (Settings → Emails); ilk dört commit'in ekip hesabında görünmesi için. Geçmiş yeniden yazılmaz.
- [ ] **QA-19** Backlog'un PO onayı ve ekip tahminleri gerçekleştiğinde kaydet.
- [ ] PR #8'i (Arda) review et. Gerekli değil: PR #8 Ahmet onayıyla merge edildi.

## Arda — Lead Software Architect and Technical Lead

- [x] **F-18** `bearerAuth`, kök `security`, `servers`, `license` eklendi; `recommended` lint 0 hata (`a34146b`).
- [x] **F-19** Tag'ler, örnekler ve temel şema alanları eklendi (`c5425a4`, `a34146b`).
- [x] **F-20** `System_Vision_and_Boundary.md` PR #8'den çıkarıldı (`c5425a4`).
- [x] **F-22** Commit'ler `ardaberkkara1` hesabına bağlı.
- [ ] PR #8 açıklamasını güncelle (hâlâ "Boundary draft" ve "validation has not been run" diyor). İsteğe bağlı: PR merge edildi.
- [x] **F-21** PR #19 (`0761004`, merge `5589968`): PR #7 merge edildikten sonra `develop`'tan yeni branch: §4.4'e "No external systems are in scope for Sprint 1 (proposed)" ve aktör–SIS etkileşim tablosu; PR "Related: #12".
- [ ] İsteğe bağlı **F-19**: `Registration` şemasına `term` / `status`.
- [ ] PR #6'yı (Barış) review et. Gerekli değil: PR #6 Ahmet onayıyla merge edildi.

## Mert — Scrum Master and Agile Process Coach

- [x] **F-03** `develop` oluşturuldu; `develop-protection` ve `main-protection` ruleset'leri aktif.
- [x] **F-07** Checklist güncellendi (PR #16, #18).
- [x] PR #4 kapatıldı; tüm açık PR'lar `develop`'a çevrildi; Issue #9–#15 açıldı ve atandı.
- [x] Onaylı PR'ları merge et: #7 (`6ad16ce`), #8 (`36c7c8f`), #6 (`1b6825b`), #19 (`5589968`).
- [ ] PR #17'deki değişiklik isteğini kaldırıp onayla (F-24 `85eec71` ile düzeltildi) ve merge et; PR #2'yi (QA raporu) review et.
- [ ] Kalan merge sırası: #17 → #2.
- [ ] `develop` → `main` PR'ını aç (2 onay gerekiyor) ve merge et.
- [ ] `main` 2 onay / `Git_Workflow.md` 1 onay tutarsızlığını eşitle.
- [ ] **F-04** İsteğe bağlı: PB-01…PB-07 için Issue'ları taslaklardan aç.
- [ ] Final teslimi Teams'te yap: takım numarası, proje adı, üyeler, repository URL'si, OpenAPI YAML, Issue/PR/commit linkleri ve Sprint 1 tag'i.

## Azra — Scrum Master and Agile Process Coach

- [x] **F-15** PR #4 kapatıldı.
- [x] **QA-09** RACI MD ↔ CSV İngilizce ve birebir aynı (`72b2f86`).
- [x] **QA-12** D-01 (RACI) ve D-02 (Mert–Azra iş bölümü), MM-01 toplantı kaydı ve 6/6 katılım (`3a18842`).
- [x] **F-24** (`85eec71`) `Sprint1_Process_Records.md`: MM-01 saati "2026-11-03 20:00–21:00 Europe/Istanbul (17:00–18:00 UTC)" olmalı; Decision Log altındaki "rulesets yok / protected=false / karışık PR hedefleri" paragrafı güncel duruma göre düzeltilmeli.
- [ ] Varsa toplantı kanıtını (ekran görüntüsü / mesaj linki) MM-01 "Evidence" alanına ekle; notları sen tuttuysan MM-01 "Recorder" alanını doldur.
- [ ] Mert'ten PR #17 için yeniden onay iste.

## Barış — DevOps and CI/CD Infrastructure Engineer

- [x] **F-17** `origin/develop`'u branch'ine merge et; `Repository_Setup.md`'de Issue #5 ve PR #6'yı bağla; erişim tablosunu `gh api .../collaborators` çıktısıyla doldur.
- [x] **F-17** "`develop` yoktur / geçici hedef `docs/sprint1-team-guides`" kısmını güncelle; `develop-protection` ve `main-protection` ruleset kanıtını ekle; belgeyi İngilizceye çevir.
- [x] PR #6 açıklamasına "Closes #5" ekle; reviewer olarak Ahmet'i ekle (`d948a11`).
- [ ] **QA-21** `develop` → `main` merge edildikten sonra `sprint-1` tag'ini ve release'i oluştur; linki checklist'e ekle.

## Ahmet — Quality Assurance and Test Automation Engineer

- [x] Altı teslim başlığı için kontrol matrisi (27 kontrol).
- [x] OpenAPI'yi Redocly ile doğrula ve backlog ile eşleştir (QA-06…QA-08; `a34146b`).
- [x] PR #1, #16, #18, #8, #7, #6 ve #19 review edildi ve onaylandı.
- [x] 2026-11-04 yeniden kontrolü raporun "Yeniden kontroller" tablosuna işlendi.
- [ ] PR #17'yi review et (F-24 düzeltmesi kontrol edildi; onay gönderilecek).
- [ ] Merge sonrası son durumu kontrol et: tek Vision/Boundary belgesi ve geçerli OpenAPI `develop` @ `5589968`'de doğrulandı; PR #17 merge'ü ve tag'in doğru commit'te olduğu kontrol edilecek.
- [ ] Kendi Issue/PR/commit linklerini Mert'e ilet.

## Önerilen merge sırası

Karar Mert'indir; bu bir öneridir.

1. Tamamlandı: PR #7 (`6ad16ce`), PR #8 (`36c7c8f`), PR #6 (`1b6825b`), PR #19 (`5589968`).
2. PR #17 (Azra): F-24 düzeltildi (`85eec71`); Mert'in yeniden onayından sonra merge edilir.
3. QA son kontrolü; PR #2 en son merge edilir.
4. `develop` → `main` PR'ı açılır, 2 onay sonrası merge edilir ve `main` üzerindeki commit'e `sprint-1` tag'i atılır.
