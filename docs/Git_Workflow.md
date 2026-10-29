# Git çalışma akışı — ekip onayına sunulan taslak

Durum: **Öneri; henüz ekipçe onaylanmadı.** Onay tarihi ve karar kaydı: [TODO].
İlgili Issue: [TODO]. Koordinasyon önerisi: Mert; teknik danışman: Arda; repository ayarları: Barış.

## Repository çalışma kuralları

İşe başlamadan README, AGENTS.md, ilgili Issue ve belgeler okunur; `git status` ve aktif branch kontrol edilir. Küçük ve tek amaçlı değişiklikler hazırlanır. Başkasının dosyası veya kaydedilmemiş değişikliği izinsiz değiştirilmez. Gerçek öğrenci verisi, parola, token ve `.env` commit edilmez. Her öğrenci kendi hesabından ve gerçek kimliğiyle katkı verir; ortak hesapla katkı sahipliği oluşturulmaz.

Mert ile Azra arasındaki önerilen ayrım: Mert GitHub Projects, Issues, sprint planlama, Git-Flow koordinasyonu ve teslim takibini; Azra RACI dokümantasyonu, toplantı tutanakları, retrospektifler ve süreç raporlarını koordine eder. Bu ayrım **onay beklemektedir**; mevcut yerel RACI ve süreç şablonları Azra'nın tamamlanmış katkısı sayılmaz.

## Branch yapısı

| Branch | Önerilen amaç | Başlangıç / PR hedefi |
| --- | --- | --- |
| `main` | İncelenmiş teslim ve sürüm geçmişi | Onaylanmış `develop` sürümü / PR ile `main` |
| `develop` | Sprint entegrasyonu | Ekip onaylı başlangıç commit'i / entegrasyon hedefi |
| `feature/<issue>-<kisa-ad>` | Ürün özelliği | `develop` / `develop` |
| `docs/<issue>-<kisa-ad>` | Belge ve süreç işi | `develop` / `develop` |
| `fix/<issue>-<kisa-ad>` | Hata düzeltmesi | `develop` / `develop` |

Mevcut hazırlık branch'i `docs/sprint1-process` bu adlandırmanın istisnasıdır; Issue bağlantısı sonradan eklenir. İnceleme sırasında `develop` yerel/uzak branch kayıtlarında yoktur. Hedef branch kullanıcıyla netleşmeden PR açılmaz; otomatik olarak `main` seçilmez. Bu çalışma `develop` oluşturmaz.

## Commit mesajları

Önerilen biçim: `type(scope): kısa açıklama`; türler `feat`, `fix`, `docs`, `test`, `chore`. Örnek: `docs(sprint1): add process and delivery templates`. Gerçek Issue numarası commit gövdesinde `Refs #<numara>` ile verilir; yer tutucu commit'e taşınmaz. Atomik commit ve doğru yazar kimliği kullanılır. Bot veya başka öğrenci adına katkı uydurulmaz.

## Pull Request açma prosedürü

1. Issue kapsamı, kabul kriterleri ve sorumlu kişi netleştirilir.
2. Çalışma ağacı kontrol edilir; kullanıcı onayından sonra uygun branch kullanılır.
3. Yalnızca ilgili dosyalar açık yollarla stage edilir; staged diff ve kontroller incelenir.
4. Bu görevde commit öncesinde değişiklikler kullanıcıya tekrar gösterilir ve onay alınır.
5. Ayrı açık push onayından sonra branch gönderilir; ardından PR açma onayı istenir.
6. Onaylı hedefe PR açılır; PR şablonu doldurulur, Issue, test/inceleme kanıtı ve belgeler eklenir. Hazır olmayan iş Draft PR olur.

Varsayılan branch dışında bir hedefe açılan PR'da Issue'nun otomatik kapanacağını varsaymayın. `Related Issue` bağlantısını ekleyin; kapanışı hedef branch ve GitHub davranışına göre doğrulayın.

## Code review kuralları

En az bir yazar dışı reviewer önerilir. Arda mimari/API, Ahmet kalite/test, Nurefşan gereksinim uyumu, Mert/Azra süreç belgeleri için danışılacak kişilerdir. Reviewer doğruluk, kapsam, kabul kriterleri, güvenlik ve kanıtları inceler. Yazar kendi PR'ını tek başına onaylayıp merge etmez. Engelleyici yorumlar çözülür; anlamlı yeni değişiklikler yeniden incelenir.

## Merge prosedürü

Öneri: görev PR'larında squash merge; kaynak commit ve review bağlantıları PR'da korunur. Sürüm PR'ında `develop` → `main` geçmişini koruyan merge commit tercih edilir. Kesin yöntem ekip onayına bağlıdır. Kabul kriterleri, review ve varsa zorunlu CI kontrolleri geçmeden merge edilmez. Merge için kullanıcıdan açık onay alınır. Sonrasında Issue/Project durumu ve teslim kanıtı güncellenir; branch silme kararı ayrıca doğrulanır.

## Conflict çözme

Önce temiz çalışma ağacı sağlanır; başkasının değişikliği reset/stash ile kendiliğinden taşınmaz. Onaylı hedefin güncel hâli alınır ve çalışma branch'ine merge edilir. Çakışan bölümler dosya sahibiyle incelenir; `ours`/`theirs` ile kör toplu seçim yapılmaz. İşaretler temizlenir, ilgili kontroller tekrarlanır ve çözüm reviewer'a bildirilir. Paylaşılan branch geçmişi yeniden yazılmaz; force push kullanılmaz.

## Branch protection önerileri

Barış, plan ve yetki uygunluğunu doğrulayarak `main` ve `develop` için PR zorunluluğu, en az bir bağımsız onay, yeni commit sonrası eski onayın düşmesi, yorumların çözülmesi, force push ve silme engeli önerisini ekibe sunar. Zorunlu status check yalnızca gerçekten kurulan CI job adıyla seçilir. Yönetici bypass yetkisi mümkün olduğunca sınırlandırılır. Bu ayarlar henüz uygulanmış değildir.

## Codex ile ortak çalışma

AGENTS.md izlenir; çıktı insan tarafından gözden geçirilir. Asistan yalnızca yetkilendirilen kapsama müdahale eder. Üretilen içerik için doğrulama ve teslim sorumluluğu öğrenciye aittir. Arda'nın OpenAPI veya Nurefşan'ın gereksinim belgeleri onların adına tamamlanmaz. Yapılmamış toplantı, test veya karar yazılmaz; bilinmeyen bilgiler `[TODO]` olur. Issue → branch → commit → PR → release/tag zinciri gerçek bağlantılarla kaydedilir.
