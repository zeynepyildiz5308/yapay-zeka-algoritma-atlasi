# Algoritma Atlası — Mevcut GitHub + Netlify sitesini güncelleme

Mevcut GitHub depon:
https://github.com/zeynepyildiz5308/yapay-zeka-algoritma-atlasi

Bağlı Netlify siten:
https://yapay-zeka-algoritma-atlasi.netlify.app

**Yeni bir repo veya yeni bir Netlify projesi oluşturma.** Mevcut depoyu güncelle.

## A) GitHub Desktop ile güncelleme (önerilen)

1. GitHub Desktop'ta **File → Clone repository** ile mevcut `zeynepyildiz5308/yapay-zeka-algoritma-atlasi` deposunu bilgisayarına klonla (daha önce klonlanmadıysa).
2. Bu ZIP'i çıkart. ZIP içindeki `index.html`, `styles.css`, `app.js`, `guides.js`, `content.js`, `favicon.svg`, `README.md`, `CHANGELOG.md`, `DEPLOY.md`, `netlify.toml` ve `codes` klasörünü **klonlanmış depo klasörünün içine** kopyala. Çakışan dosyaları güncelle/üzerine yaz.
3. GitHub Desktop'ta değişiklikleri kontrol et; `Summary` alanına `Öğrenme deneyimi ve anlatım güncellemesi` yaz.
4. **Commit to main** → **Push origin**.
5. Netlify'da **Deploys** bölümünden yeni üretim dağıtımını kontrol et.
6. Siteyi `Ctrl + Shift + R` ile önbelleği atlayarak yenile.

## B) Git Bash terminali ile güncelleme

Aşağıdaki `git clone` işlemini yalnızca bu depoyu henüz indirmediysen yap:

```bash
git clone https://github.com/zeynepyildiz5308/yapay-zeka-algoritma-atlasi.git
cd yapay-zeka-algoritma-atlasi
```

Ardından güncellenen ZIP dosyalarını bu klasöre kopyala. Terminal depo klasöründeyken:

```bash
git status
git add -A
git commit -m "Algoritma Atlasi v2: anlatim ve kullanim iyilestirmeleri"
git push origin main
```

Önce `git status` ile değişen dosyaları incele; başka birinin yaptığı değişiklik varsa üzerine yazmadan önce karşılaştır.

## C) GitHub web arayüzüyle

GitHub'ın **Add file → Upload files** yoluyla ZIP içindeki dosyaları (ZIP arşivini değil) yükleyebilirsin. Var olan dosyalarda güncelleme/çakışma uyarısı görürsen yeni içerikle eskisinin değiştirileceğini kontrol et. `guides.js` dosyasının repo ana dizininde bulunması şarttır. `Commit changes` işlemini `main` dalında tamamla.

## Netlify'da yeni ayar gerekiyor mu?

Hayır. V2 de aynı statik HTML/CSS/JavaScript yapısını kullanıyor; `netlify.toml` içinde `publish = "."` korunuyor. GitHub bağlantısı kurulu olduğundan `main` dalına gönderilen yeni commit üretim sitesine yeniden dağıtım tetikler.

## Güncelleme sonrası kontrol

- Ana sayfa açılıyor ve **Kaldığın yerden devam et** alanı görünüyor.
- Bir derste **Adım adım** sekmesi çalışıyor; aynı dersin içinde kalıyorsun.
- **Kodda ilgili satıra git** kartı kaynak kodu kaydırıyor.
- **Performans / Yazılım projelerinde kullanım** bölümleri görünüyor.
- **7 konu**, demolar, Python dosyaları ve kaynak bağlantıları yerinde.
- Mobil görünümde ders içi bölüm çubuğu yatay kaydırılabiliyor.

### Önceki ilerleme kaybolur mu?

Hayır; aynı tarayıcıda ve aynı site alan adında `atlas-done` localStorage anahtarı korunuyor. Gizli sekmede veya başka cihazda bu ilerleme otomatik taşınmaz.
