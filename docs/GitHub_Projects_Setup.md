# GitHub Projects kurulumu ve Sprint 1 takibi

**Ekip onayına sunulan öneri.** Bu belge uzak kaynak oluşturmaz veya ayar uygulamaz. Mert takip, Barış altyapı/erişim, Nurefşan ürün kapsamı için önerilen sorumlulardır. GitHub CLI (`gh`) yerelde bulunamadı; mevcut uzak Issues, PR'lar ve Projects incelenmedi. Git remote kişisel repository'yi gösteriyor; bu, Organization kurulduğunu kanıtlamaz.

## Pano durumları

| Status | Giriş / çıkış ölçütü |
| --- | --- |
| Backlog | Öneri kaydedildi; PO/ekip kapsam kararı ve ayrıntılandırma bekleniyor |
| To Do | Kapsam, sorumlu, kabul kriteri ve bağımlılıklar net; sprint'e alındı |
| In Progress | Sorumlu çalışmaya başladı; Issue/branch bağlantısı eklendi |
| In Review | İncelenebilir PR veya belge ve kontrol kanıtları hazır |
| Done | Kabul kriterleri, bağımsız review ve ilgili kontroller tamam; gerekiyorsa PR merge edildi ve kanıt bağlandı |

Engel varsa Status yanında ayrı `Blocked` alanı ve engel bağlantısı kullanılması önerilir. Hazır şablon dosyası bütün Sprint 1 teslimini Done yapmaz.

## Önerilen alanlar ve görünümler

Status, Assignees (gerçek GitHub hesapları [TODO]), Priority (P1/P2/P3), Story Points (Number), Sprint (Sprint 1), Epic, Requirement, Dependencies, Evidence ve Blocked. İş kimlikleri S1-01…S1-16 ile korunur; gerçek Issue numarası yerine geçmez. Board görünümü Status'a göre; tablo görünümü sorumlu, öncelik, sprint ve kanıt alanlarıyla düzenlenir. Varsayılan durum önerisi Backlog'dur.

## Sprint 1 görev listesi

Tüm atamalar öneridir. Şu an yalnızca yerel süreç taslakları vardır; uzak Issue veya atama yapılmamıştır. A/R ayrıntıları [RACI](RACI_Matrix.md) ile aynıdır.

| ID | Görev | Önerilen sorumlu (R) | Kabul kriterleri |
| --- | --- | --- | --- |
| S1-01 | Proposal ve problem tanımı | Nurefşan | Problem, amaç, paydaşlar ve kapsam belgelenmiş; ekip/PO incelemesi kayıtlı |
| S1-02 | Lisans kararı | Nurefşan, Arda | Mevcut MIT dosyası incelenmiş; seçim gerekçesi proposal'a eklenmiş; karar kayıtlı |
| S1-03 | System Vision | Nurefşan, Arda | Sistem hedefleri ve paydaş ihtiyaçları açıklanmış; proposal ile uyumlu |
| S1-04 | System Boundary | Arda, Nurefşan | Aktörler, dış sistemler, kapsam içi/dışı açık; vision ile uyumlu |
| S1-05 | Draft OpenAPI YAML | Arda | YAML parse ediliyor; seçilen OpenAPI sürümüne göre doğrulanmış; gereksinim eşlemesi ve taslak sınırlamaları yazılı |
| S1-06 | Roller ve RACI | Azra, Mert | Altı üye mevcut; her satır tek A; CSV/Markdown aynı; ekip onayı kayıtlı |
| S1-07 | Organization/repository erişimleri | Barış, Mert | Org kararı alınmış; altı üyenin hesap/erişimleri ve repository URL'si doğrulanmış |
| S1-08 | Git-Flow ve review politikası | Mert, Barış | Branch, commit, PR, review, merge, conflict ve protection kuralları incelenmiş; develop kararı kayıtlı |
| S1-09 | Initial Product Backlog | Nurefşan, Mert | Hikâye, kabul kriteri, öncelik, tahmin ve bağımlılıklar PO/ekipçe incelenmiş; taslak/onay ayrımı açık |
| S1-10 | Projects, Issues ve sprint planı | Mert, Azra | İzin sonrası pano ve gerçek Issue bağlantıları mevcut; sorumlular, sprint hedefi ve durumlar doğrulanmış |
| S1-11 | Issue/PR şablonları ve AGENTS | Mert | Üç Issue ve bir PR şablonu alanları tam; güvenlik ve onay sınırları açık; review yapılmış |
| S1-12 | Süreç kayıtları | Azra, Mert | Gerçek toplantı/katılım/karar/aksiyon kayıtları kanıtlı; yapılmayanlar açıkça boş/planlandı |
| S1-13 | Kalite ve teslim uygunluğu | Ahmet, Arda, Mert | Beş resmî teslim ve bağlantıları kontrol edilmiş; eksikler ve sonuç kayıtlı |
| S1-14 | Bireysel katkı kanıtları | Altı üye | Her üyenin gerçek hesabı, Issue, PR/review ve commit kanıtları eşlenmiş |
| S1-15 | Release/tag | Barış, Mert | Kullanıcı onayı sonrası incelenmiş commit'e sürüm verilmiş; URL ve SHA kaydedilmiş |
| S1-16 | Final teslim takibi | Mert, Azra, Barış | Kontrol listesi kapatılmış; teslim bağlantıları ve ders kanalındaki teslim kanıtı kayıtlı |

## GitHub arayüzünden adımlar — yalnızca onay sonrası

1. Mevcut Organization/Projects ve repository erişimlerini kontrol edin; mevcut panoyu gereksiz yere çoğaltmayın. Org oluşturma veya repository taşıma ayrı ekip/yetki kararıdır.
2. Uygun owner altında Projects üzerinden yeni pano açın veya mevcut panoyu seçin. Repository'yle ilişkilendirin.
3. Status alanını yukarıdaki beş seçenekle düzenleyin. Gerekli ek alanları ekleyin; Board'u Status'a göre gruplayın.
4. Üyelerin erişimlerini Barış doğrulasın. Ekip onayından sonra S1 görevlerini Issue şablonlarıyla açın; gerçek assignee, kabul kriterleri ve bağımlılık bağlantılarını ekleyin.
5. Issue'ları panoya ekleyin. Sprint 1 kapsamını S1 işleriyle seçin; PB ürün örneklerini otomatik olarak uygulama taahhüdüne dönüştürmeyin.
6. Projects Workflows ayarlarını inceleyin. Issue kapanması/PR merge edilmesiyle Done durumuna geçiren varsayılan otomasyonları kontrol edin; kabul edilmeyen veya iptal edilen işi yanlışlıkla tamamlandı saymayın. İlk aşamada geçişleri elle doğrulayın.
7. Mert ilerleme/engel takibini, Azra gerçekleşen toplantı ve karar kayıtlarını güncellesin. Teslimde gerçek Issue → PR → commit → release/tag bağlantılarını kontrol edin.

## CLI mevcut olduğunda salt okunur kontrol örnekleri

Kurulum veya giriş bu görevde yapılmadı. Aşağıdaki PowerShell komutları CLI kurulduktan ve hesap yetkilendirildikten sonra mevcut durumu kontrol eder. Project owner Organization ise örnekteki kişisel owner'ı doğrulanmış Organization adıyla değiştirin.

```powershell
gh --version
gh auth status
gh repo view mert494/student-information-system
gh issue list --repo mert494/student-information-system --state all --limit 100
gh pr list --repo mert494/student-information-system --state all --limit 100
gh project list --owner mert494
```

Project numarası belirlendikten sonra `gh project view <NUMBER> --owner <OWNER>` ve `gh project item-list <NUMBER> --owner <OWNER>` kullanılır; `<...>` alanları gerçek değerlerle değiştirilmeden çalıştırılmaz. Listeleme sayfalaması/sınırları nedeniyle ilk sonuçları bütün kayıtlar sanmayın. Erişim hatasını “pano yok” olarak yorumlamayın. Project okuma için gereken hesap izinleri CLI yardımına göre doğrulanır; yetki genişletme ve uzak değişiklikler bu hazırlığın kapsamı dışındadır.

Issue, Project, release, branch protection veya başka uzak kaynağı değiştiren komutlar burada çalıştırılmaz. Push için açık onay, ardından PR açmak için ayrı onay gerekir. `develop` yoksa PR hedefi kullanıcıya sorulur.

## Kaynaklar

- [GitHub Projects single-select alanları](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields)
- [GitHub Projects yerleşik otomasyonları](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)
- [GitHub CLI project komutları](https://cli.github.com/manual/gh_project)
