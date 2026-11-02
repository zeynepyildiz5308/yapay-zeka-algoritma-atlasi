# GitHub → Netlify: Adım adım yayımlama

## A. GitHub'a yükle

1. İndirdiğin `Yapay_Zeka_Algoritma_Atlasi_Netlify.zip` dosyasını bilgisayarına çıkar.
2. GitHub'da **New repository** üzerinden örneğin `yapay-zeka-algoritma-atlasi` adlı bir depo oluştur.
3. Yeni deponun **Add file → Upload files** menüsüne gir.
4. ZIP'in **içindeki dosyaların tamamını** yükle. Önemli: `index.html` dosyası deponun en üst dizininde olmalı; iç içe klasörde kalmamalı.
5. **Commit changes** ile kaydet.

Alternatif olarak, bilgisayarında Git kuruluysa çıkardığın klasörde terminal açıp:

```bash
git init
git add .
git commit -m "Yapay zeka giris ders atlasini ekle"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADIN/yapay-zeka-algoritma-atlasi.git
git push -u origin main
```

`KULLANICI_ADIN` kısmını kendi GitHub kullanıcı adınla değiştir. Depoyu GitHub'da önceden oluştur.

## B. Netlify'a bağla

1. [app.netlify.com](https://app.netlify.com/) adresini aç ve giriş yap.
2. **Add new project → Import an existing project** seç.
3. **GitHub** sağlayıcısını seçip ilgili depoya erişim izni ver.
4. Yüklediğin depoyu seç.
5. Ayarlar:
   - **Branch:** `main`
   - **Base directory:** boş
   - **Build command:** boş (gerek yok)
   - **Publish directory:** `.` (nokta)
6. **Deploy** ile yayımla.

`netlify.toml` içindeki `publish = "."` ayarı da bu yapılandırmayı ifade eder.

## C. Güncelleme

Bir ders metnini değiştirmek için `content.js`, görsel biçimi değiştirmek için `styles.css`, etkileşim değiştirmek için `app.js` düzenlenir. Güncellenmiş dosyaları GitHub'da commit ettiğinde Netlify aynı depodan yeni sürümü yayımlar.

## D. Sık görülen sorunlar

**Beyaz sayfa:** Tarayıcının geliştirici konsoluna (F12) bak; `content.js` veya `app.js` yüklenemiyor olabilir. Dosya adlarını ve GitHub depo kökünü kontrol et.

**Python kodları görünmüyor:** `codes/` klasörünün ve içindeki `.py` dosyalarının da GitHub'a yüklendiğinden emin ol. Dosya adlarında büyük-küçük harfe dikkat et.

**index.html dosyası yerelde çift tıklayınca kodlar görünmüyor:** Tarayıcı `file://` üzerinden `fetch()` işlemini engelleyebilir. Yerel sunucu çalıştır: `python -m http.server 8000` veya doğrudan Netlify sürümünü kullan.

**Dış bağlantılar çalışmıyor:** Ders videoları/harici kaynaklar üçüncü taraf sitelerde bulunuyor; zaman içinde adres veya erişim şartı değişebilir.

**Güvenlik:** Sitede kullanıcı girişi, şifre veya API anahtarı bulunmuyor. İlerleme verileri yalnızca aynı tarayıcıda saklanır.
