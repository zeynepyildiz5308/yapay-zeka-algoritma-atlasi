# Algoritma Atlası · Sürüm 2 — Öğrenme deneyimi iyileştirmeleri

## Neler değişti?

- **Ders içi gezinme hatası giderildi.** Eski `href="#..."` bağlantıları hash yönlendiricisini bozabiliyordu. Şimdi bölüm düğmeleri sayfanın doğru yerine ilerliyor; mevcut ders açık kalıyor.
- **Sabit bölüm çubuğu ve okuma ilerleme göstergesi** eklendi. Okur bulunduğu bölümü görebiliyor.
- **7 dersin tamamına ayrıntılı yazılım öğrencisi anlatımları** eklendi: ön koşullar, kavramın kısa özeti, sezgisel benzetme, beş adımlı işlem izleme, sözde kod, maliyet / karmaşıklık, gerçek dünya kullanımı, hata ayıklama, temel çıkarımlar ve cevaplı düşünme sorusu.
- **Python kodu açıklamalarına tıklayınca ilgili satıra gitme** özelliği eklendi; kodun tam hâli ve indirme bağlantısı korundu.
- **Ana sayfada kaldığın derse devam et** alanı eklendi. Mevcut tarayıcıdaki ilerleme saklama davranışı korundu.
- **Kısa testlerin puan geri bildirimi** eklendi.
- Erişilebilir klavye odağı, atlama düğmesi, mobil ders çubuğu ve koyu tema uyumu iyileştirildi.
- Türkçe Python resmî belgeleri, AST, CS50 Minimax gibi **ek öğrenme kaynakları** yerleştirildi.
- Kurulumsuz statik site yapısı; orijinal 7 Python dosyası, mevcut görsel laboratuvarlar ve mevcut renk teması korundu.

## İçerik ilkesi

`codes/*.py` dosyaları değişmedi. Pedagojik genişletme `guides.js` içindedir. Tarayıcıdaki simülasyonlar Python kodunu çalıştırmaz; öğretici JavaScript sürümleridir. Bazı uygulamalar (ör. puzzle visited kontrolü) öğretim amacıyla kaynak koddan farklı olabilir; derste belirtilir.

## Kurulum

**Mevcut GitHub deposunu güncellemek için:** [`DEPLOY.md`](DEPLOY.md) dosyasını izle. Yalnızca `index.html`, `styles.css`, `app.js`, yeni `guides.js` ve ek belge dosyaları değişti; `content.js`, `codes/` ve Netlify ayarları önceki sürümle uyumludur.
