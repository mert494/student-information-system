# Initial Product Backlog — içerik onayı bekleyen taslak

**Bütün hikâyeler örnektir; Product Owner Nurefşan onaylayana kadar ürün gereksinimi veya Sprint 1 taahhüdü değildir.** Mert yalnızca GitHub takibi için hazırlamıştır. Sprint 1'de hedef backlog taslağıdır; aşağıdaki özelliklerin uygulanması taahhüt edilmez.

P1 = yüksek, P2 = orta, P3 = düşük öncelik önerisi. Story Points göreli efor/belirsizlik tahminidir, saat değildir; ekip yeniden tahminler. Proposed Owner önerileri gerçek atama değildir. Özel geliştirme görevleri mevcut resmî rollerin yerine geçmez. REQ kimlikleri ve OpenAPI eşleştirmeleri Nurefşan/Arda ile [TODO]; hiçbir endpoint burada belirlenmez.

## PB-01 — Kullanıcı girişi (örnek)

- **Epic:** Kimlik ve erişim
- **User Story:** Bir kullanıcı olarak hesabımla giriş yaparak yetkili olduğum işlemlere erişmek istiyorum.
- **Acceptance Criteria:** Geçerli test hesabı giriş yapabilir; yanlış bilgilerde erişim reddedilir ve hesabın varlığını açığa çıkarmayan mesaj gösterilir; çıkıştan sonra korunan işlem tekrar kimlik doğrulama ister.
- **Priority:** P1 (öneri)
- **Story Points (öneri):** 5
- **Dependencies:** PO tarafından onaylı kimlik gereksinimleri; Arda'nın sözleşmesi; test hesabı politikası [TODO].
- **Proposed Owner:** Arda; kalite danışmanı Ahmet. Atama onayı [TODO].

## PB-02 — Rol bazlı yetkilendirme (örnek)

- **Epic:** Kimlik ve erişim
- **User Story:** Sistem yöneticisi olarak öğrenci, akademisyen ve yönetici işlemlerini role göre sınırlamak istiyorum.
- **Acceptance Criteria:** PO'nun onayladığı rol/izin tablosu uygulanır; yetkisiz doğrudan API isteği reddedilir; bir öğrencinin başka öğrencinin korunan verisine erişimi reddedilir.
- **Priority:** P1 (öneri)
- **Story Points (öneri):** 5
- **Dependencies:** PB-01; rol ve veri erişim kurallarının PO onayı [TODO].
- **Proposed Owner:** Arda; olumsuz senaryolar Ahmet. Atama onayı [TODO].

## PB-03 — Öğrenci yönetimi (örnek)

- **Epic:** Öğrenci işleri
- **User Story:** Yetkili yönetici olarak öğrenci kayıtlarını oluşturmak, listelemek ve güncellemek istiyorum.
- **Acceptance Criteria:** Zorunlu alanlar doğrulanır; aynı öğrenci numarasıyla ikinci kayıt reddedilir; yetkisiz kullanıcı kayıt değiştiremez; güncelleme listeye yansır.
- **Priority:** P1 (öneri)
- **Story Points (öneri):** 5
- **Dependencies:** PB-02; öğrenci veri alanları ve yaşam döngüsü PO onayı [TODO].
- **Proposed Owner:** Arda (uygulayıcı ekipçe netleştirilecek); kabul senaryoları Nurefşan. Atama onayı [TODO].

## PB-04 — Ders yönetimi (örnek)

- **Epic:** Ders kataloğu
- **User Story:** Yetkili yönetici olarak dersleri tanımlamak ve güncellemek istiyorum.
- **Acceptance Criteria:** Zorunlu ders alanları doğrulanır; aynı kapsamda yinelenen ders kodu reddedilir; yetkisiz değişiklik engellenir; kayıtlı ders listelenebilir.
- **Priority:** P1 (öneri)
- **Story Points (öneri):** 5
- **Dependencies:** PB-02; ders/dönem modeli ve benzersizlik kapsamı PO onayı [TODO].
- **Proposed Owner:** Arda (uygulayıcı ekipçe netleştirilecek); kalite danışmanı Ahmet. Atama onayı [TODO].

## PB-05 — Ders kayıt işlemleri (örnek)

- **Epic:** Ders kaydı
- **User Story:** Öğrenci olarak uygun dönemde bir derse kayıt olmak ve kayıtlarımı görmek istiyorum.
- **Acceptance Criteria:** Uygun öğrenci açık derse kayıt olabilir; aynı öğrenci/ders/dönem için ikinci kayıt engellenir; kapalı kayıt döneminde işlem reddedilir; kayıt yalnızca ilgili öğrencinin listesinde görünür.
- **Priority:** P1 (öneri)
- **Story Points (öneri):** 8
- **Dependencies:** PB-03, PB-04; dönem, kontenjan ve önkoşul kapsamının PO kararı [TODO].
- **Proposed Owner:** Arda; kural danışmanı Nurefşan; doğrulama Ahmet. Atama onayı [TODO].

## PB-06 — Akademisyen not girişi (örnek)

- **Epic:** Not yönetimi
- **User Story:** Akademisyen olarak sorumlu olduğum dersin kayıtlı öğrencilerine not girmek istiyorum.
- **Acceptance Criteria:** Yalnızca atanmış akademisyen ilgili derse not girebilir; onaylı aralık dışındaki değer reddedilir; kayıtlı olmayan öğrenciye not girilemez; kaydedilen not tekrar okunabilir.
- **Priority:** P2 (öneri)
- **Story Points (öneri):** 8
- **Dependencies:** PB-02, PB-05; akademisyen/ders ataması; not ölçeği ve yayımlama kuralları PO onayı [TODO].
- **Proposed Owner:** Arda; kabul senaryoları Nurefşan ve Ahmet. Atama onayı [TODO].

## PB-07 — Öğrenci not görüntüleme (örnek)

- **Epic:** Not yönetimi
- **User Story:** Öğrenci olarak kendi derslerimde yayımlanmış notlarımı görmek istiyorum.
- **Acceptance Criteria:** Öğrenci yalnızca kendi yayımlanmış notlarını görür; yayımlanmamış not gösterilmez; veri yoksa anlaşılır boş durum gösterilir; başka öğrencinin notuna doğrudan istek reddedilir.
- **Priority:** P2 (öneri)
- **Story Points (öneri):** 3
- **Dependencies:** PB-06; yayımlama kuralı ve görünür alanlar PO onayı [TODO].
- **Proposed Owner:** Arda (uygulayıcı ekipçe netleştirilecek); doğrulama Ahmet. Atama onayı [TODO].

## Projects'e aktarım ve onay

Nurefşan kapsamı, hikâyeleri ve öncelikleri inceler; ekip puanları ve uygulayıcıları netleştirir. Mert yalnızca uzak kaynak oluşturma izninden sonra gerçek Issue'ları açar ve PB kimliklerini gerçek Issue bağlantılarıyla eşler. Onaylanan gereksinim kimlikleri, bağımlılıklar, sorumlu ve kabul kriterleri her Issue'ya eklenir. Genel DoD önerisi: kabul kriterleri doğrulandı, ilgili testler geçti, belgeler güncellendi, bağımsız review tamamlandı ve onaylı PR merge edildi. Onay kaydı: [TODO].
