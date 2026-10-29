# Repository çalışma kuralları

Bu kurallar bu repository üzerinde çalışan Codex ve diğer kod asistanları içindir.

- Değişiklikten önce proje yapısını, README, ilgili belgeleri, `git status` ve branch'leri incele. Alt dizinlerdeki AGENTS.md kurallarını da oku.
- Mevcut mimariye ve ekipçe kabul edilmiş kararlara uy. Taslakları onaylanmış karar gibi kullanma.
- OpenAPI sözleşmesi mevcutsa ona uy; bulunmuyorsa veya belirsizse Arda ile netleştir. Sözleşmeyi kendi varsayımınla tamamlanmış ilan etme.
- Başkasının dosyalarını veya kaydedilmemiş değişikliklerini izinsiz değiştirme, silme ya da üzerine yazma. Çakışan çalışma varsa dur ve kullanıcıya bildir.
- Çalışmayı ilgili Issue ile ilişkilendir. Issue yoksa `[TODO]` kullan; numara veya bağlantı uydurma. Uzak kaynak oluşturmak için açık kullanıcı onayı al.
- İlgili test ve kontrolleri çalıştır; çalıştırılamayanları ve nedenlerini raporla. Belge işlerinde bağlantı, tablo, şablon ve tutarlılık kontrolü yap.
- Görev dışı refactoring, bağımlılık güncellemesi veya toplu biçimlendirme yapma.
- Güvenlik sırlarını, erişim token'larını ve `.env` dosyalarını commit etme; örneklerde yalnızca sahte değerler kullan. Stage öncesinde dosyaları kontrol et.
- Her öğrenci kendi GitHub hesabıyla katkı verir. Başka birinin kimliğiyle commit üretme; gerçek katkıları Issue, PR ve commit kanıtlarıyla kaydet.
- Bu Sprint 1 hazırlığında ilk aşama yalnızca yerel dosya düzenlemesidir. Branch oluşturma/değiştirme, stage ve commit için kullanıcı onayını bekle; `main` veya `develop` üzerinde doğrudan commit yapma.
- Push ve merge öncesinde açık kullanıcı onayı al. Push onayını PR açma veya merge onayı sayma; PR açmadan önce ayrıca onay al. Force push yapma.
- Raporlarda yapılan işlemlerle önerileri ayır; yapılmamış toplantı, test, atama veya teslimi tamamlandı gösterme.
