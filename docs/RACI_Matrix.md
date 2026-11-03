# Sprint 1 RACI matrisi

**Ekip onayı gereken taslak.** Onay tarihi / Decision ID: [TODO]. Bu dosya Mert'in süreç hazırlığı için oluşturulan öneridir; Azra'nın incelemesi ve ekip mutabakatı beklenir.

R = Responsible (işi yapan), A = Accountable (sonuçtan hesap veren), C = Consulted (danışılan), I = Informed (bilgilendirilen). `A/R` aynı kişinin iki rolü üstlenmesidir. Her satırda tam bir A vardır; atamalar yapılmış kabul edilmez.

| Üye | Resmî rol | Önerilen süreç odağı |
| --- | --- | --- |
| Arda | Lead Software Architect and Technical Lead | Mimari, sistem sınırı ve OpenAPI |
| Barış | DevOps and CI/CD Infrastructure Engineer | GitHub altyapısı ve repository ayarları |
| Ahmet | Quality Assurance and Test Automation Engineer | Doğrulama ve kabul kriterleri |
| Mert | Scrum Master and Agile Process Coach | Projects, Issues, sprint planlama, Git-Flow, teslim takibi |
| Azra | Scrum Master and Agile Process Coach | RACI, tutanak, retrospektif, süreç raporu |
| Nurefşan | Product Owner and Requirements Engineer | Problem, ürün kapsamı ve backlog onayı |

Mert–Azra ayrımı henüz onaylanmamış öneridir.

| ID | Görev / teslim | Arda | Barış | Ahmet | Mert | Azra | Nurefşan |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-01 | Project Proposal and Problem Definition | C | I | C | C | I | A/R |
| S1-02 | Açık kaynak lisans seçimi ve gerekçesi | R | C | I | C | I | A/R |
| S1-03 | System Vision | R | I | C | C | I | A/R |
| S1-04 | System Boundary Specification | A/R | C | C | I | I | R |
| S1-05 | Draft OpenAPI YAML Contract | A/R | C | C | I | I | C |
| S1-06 | Team Role Assignments and RACI Matrix | C | C | C | R | A/R | C |
| S1-07 | GitHub Organization ve repository erişimleri | C | A/R | I | R | I | C |
| S1-08 | Git-Flow kuralları ve review politikası | C | R | C | A/R | C | I |
| S1-09 | Initial Product Backlog içerik ve öncelik onayı | C | C | C | R | C | A/R |
| S1-10 | Projects, Issues ve sprint planlama | C | C | C | A/R | R | C |
| S1-11 | Issue ve PR şablonları, AGENTS kuralları | C | C | C | A/R | C | I |
| S1-12 | Toplantı kayıtları, review ve retrospektif raporu | I | I | C | R | A/R | C |
| S1-13 | Sprint 1 kalite ve teslim uygunluk kontrolü | R | C | A/R | R | C | C |
| S1-14 | Issue, PR ve bireysel commit kanıtlarının takibi | R | R | R | A/R | R | R |
| S1-15 | Sprint 1 release ve tag hazırlığı | C | A/R | C | R | I | C |
| S1-16 | Final teslim bağlantıları ve teslim takibi | C | R | C | A/R | R | C |

CSV eşleniği: [RACI_Matrix.csv](RACI_Matrix.csv). CSV UTF-8 BOM ve virgül ayırıcı kullanır; Excel'de gerekirse Veri → Metin/CSV'den, UTF-8 ve virgül seçilir. Belgelerdeki S1 kimlikleri yerel takip kimlikleridir, GitHub Issue numarası değildir.
