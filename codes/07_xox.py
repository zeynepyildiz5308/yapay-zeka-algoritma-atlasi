# -*- coding: utf-8 -*-  # Türkçe karakterlerin dosyada doğru kullanılmasını sağlar.

import numpy as np                 # Matris oluşturmak ve sayısal işlemler yapmak için NumPy.
import matplotlib.pyplot as plt    # Oyun tahtasını çizmek ve fare tıklamalarını almak için Matplotlib.

# 1. OYUNUN BAŞLANGIÇ DEĞERLERİ
N = 3                             # Tahta 3 satır ve 3 sütundan oluşur.
a = np.zeros((N, N), dtype=int)    # Bütün kareleri başlangıçta 0 (boş) olan bir matris oluşturur.
bil = 1                           # Bilgisayarın işareti X'tir; matriste 1 ile tutulur.
siz = -1                          # Oyuncunun işareti O'dur; matriste -1 ile tutulur.


# 2. OYUN TAHTASINI ÇİZEN FONKSİYON
def tahta_ciz(tahta):              # Verilen matrisi görsel XOX tahtasına dönüştürür.
    n, _ = tahta.shape            # Satır sayısını n değişkenine alır; sütun sayısını kullanmaz.
    plt.clf()                     # Önceki çizimi temizler; tahtanın üst üste çizilmesini önler.
    plt.axis((0, n, n, 0))        # Eksenleri ayarlar; 0. satırın yukarıda olmasını sağlar.
    plt.grid(True)                # Kareleri ayıran ızgara çizgilerini gösterir.
    plt.xticks(np.arange(n + 1))  # Yatay eksene 0, 1, 2, 3 çizgi konumlarını yerleştirir.
    plt.yticks(np.arange(n + 1))  # Dikey eksene 0, 1, 2, 3 çizgi konumlarını yerleştirir.

    for i in range(n):            # Tahtanın satırlarında dolaşır (i: satır numarası).
        for j in range(n):        # Her satırın sütunlarında dolaşır (j: sütun numarası).
            if tahta[i, j] == bil:  # Karede bilgisayarın değeri 1 varsa...
                plt.text(j + 0.5, i + 0.5, "X", va="center", ha="center", fontsize=30)  # X'i karenin ortasına yazar.
            elif tahta[i, j] == siz:  # Karede oyuncunun değeri -1 varsa...
                plt.text(j + 0.5, i + 0.5, "O", va="center", ha="center", fontsize=30)  # O'yu karenin ortasına yazar.

    plt.draw()                    # Güncellenmiş tahtayı yeniden çizer.
    plt.pause(0.01)               # Grafik penceresinin çizimi işlemesine kısa süre tanır.


# 3. KAZANANI BELİRLEYEN FONKSİYON
def sonuc(tahta):                  # Satır, sütun ve çaprazlardaki üçlüleri kontrol eder.
    n, _ = tahta.shape            # Tahtanın satır sayısını alır.

    for k in range(n):            # Her satır ve sütunu sırayla kontrol eder.
        if np.all(tahta[k, :] == siz):  # k. satırın bütün hücreleri -1 (O) mu?
            return -10            # Evetse oyuncu kazanmıştır.
        if np.all(tahta[k, :] == bil):  # k. satırın bütün hücreleri 1 (X) mi?
            return 10             # Evetse bilgisayar kazanmıştır.

        if np.all(tahta[:, k] == siz):  # k. sütunun bütün hücreleri -1 (O) mu?
            return -10            # Evetse oyuncu kazanmıştır.
        if np.all(tahta[:, k] == bil):  # k. sütunun bütün hücreleri 1 (X) mi?
            return 10             # Evetse bilgisayar kazanmıştır.

    c = np.array([tahta[k, k] for k in range(n)])  # Sol üstten sağ alta ana köşegenin değerlerini alır.
    if np.all(c == siz):          # Ana köşegendeki bütün işaretler O mu?
        return -10                # Oyuncu kazanmıştır.
    if np.all(c == bil):          # Ana köşegendeki bütün işaretler X mi?
        return 10                 # Bilgisayar kazanmıştır.

    c = np.array([tahta[k, n - 1 - k] for k in range(n)])  # Sağ üstten sol alta diğer köşegeni alır.
    if np.all(c == siz):          # Diğer köşegendeki bütün işaretler O mu?
        return -10                # Oyuncu kazanmıştır.
    if np.all(c == bil):          # Diğer köşegendeki bütün işaretler X mi?
        return 10                 # Bilgisayar kazanmıştır.

    return 0                      # Kazanan yoksa 0 döndürür; oyun devam edebilir.


# 4. BOŞ KARE KALIP KALMADIĞINI KONTROL EDEN FONKSİYON
def hamle_varmi(tahta):           # Oyunun devam edebileceği boş bir kare arar.
    if np.any(tahta == 0):        # Matrisin en az bir elemanı 0 (boş) mu?
        return True               # Evetse yeni bir hamle yapılabilir.
    return False                  # Boş kare kalmadıysa yeni hamle yapılamaz.


# 5. OYUNU BAŞLATMA VE OYUNCU-BİLGİSAYAR HAMLELERİ
fig = plt.figure(figsize=(6, 6))  # 6 × 6 inç boyutunda bir grafik penceresi açar.
tahta_ciz(a)                      # Başlangıçtaki boş tahtayı ekranda gösterir.

while plt.fignum_exists(fig.number):  # Grafik penceresi açık olduğu sürece oyunu sürdürür.
    xy = plt.ginput(1, timeout=-1)  # Oyuncunun tahtaya bir kez tıklamasını bekler (süre sınırı yoktur).
    if not xy:                    # Pencere kapatılırsa veya tıklama alınamazsa...
        break                     # Oyun döngüsünü sonlandırır.

    x = int(np.floor(xy[0][0]))  # Tıklamanın yatay konumunu sütuna çevirir; negatif konumu da doğru işler.
    y = int(np.floor(xy[0][1]))  # Tıklamanın dikey konumunu satıra çevirir; negatif konumu da doğru işler.

    if not (0 <= x < N and 0 <= y < N):  # Tıklama 3 × 3 oyun alanının dışında mı?
        plt.title("Yanlış Hamle: Tahtanın içine tıklayın!")  # Hata mesajı gösterir.
        plt.draw()                # Hata başlığını görüntüler.
        plt.pause(1)              # Mesajın okunabilmesi için 1 saniye bekler.
        tahta_ciz(a)              # Geçerli tahtayı yeniden gösterir.
        continue                  # Geçersiz tıklamayı atlar; tekrar hamle bekler.

    if a[y, x] != 0:              # Tıklanan kare daha önce doldurulmuş mu?
        plt.title("Yanlış Hamle: Dolu kare seçtiniz!")  # Hata mesajı gösterir.
        plt.draw()                # Hata başlığını görüntüler.
        plt.pause(1)              # Mesajın okunabilmesi için 1 saniye bekler.
        tahta_ciz(a)              # Geçerli tahtayı yeniden gösterir.
        continue                  # Dolu kareyi değiştirmeden yeni tıklama bekler.

    a[y, x] = siz                 # Oyuncunun seçtiği boş kareye -1 (O) yerleştirir.
    tahta_ciz(a)                  # Oyuncunun O işaretini tahtada gösterir.

    if sonuc(a) == -10:           # Oyuncu üç O'yu yan yana getirdi mi?
        plt.title("Tebrikler kazandınız!")  # Kazanma mesajını gösterir.
        plt.draw()                # Kazanma mesajını ekranda günceller.
        break                     # Oyunu bitirir.

    if not hamle_varmi(a):        # Oyuncu hamlesinden sonra boş kare kalmadı mı?
        plt.title("Berabere kaldınız")  # Beraberlik mesajını gösterir.
        plt.draw()                # Mesajı ekrana yansıtır.
        break                     # Oyunu bitirir.

    while True:                   # Bilgisayar boş kare bulana kadar rastgele seçim yapar.
        x, y = np.random.randint(0, N, size=2)  # 0, 1 veya 2 arasından rastgele sütun ve satır seçer.
        if a[y, x] == 0:          # Seçilen kare boş mu?
            break                 # Boşsa rastgele seçim döngüsünden çıkar.

    a[y, x] = bil                 # Bilgisayarın seçtiği boş kareye 1 (X) yerleştirir.
    tahta_ciz(a)                  # Bilgisayarın X işaretini tahtada gösterir.

    if sonuc(a) == 10:            # Bilgisayar üç X'i yan yana getirdi mi?
        plt.title("Bilgisayar kazandı")  # Bilgisayarın kazandığını bildirir.
        plt.draw()                # Kazanma mesajını ekranda günceller.
        break                     # Oyunu bitirir.

    if not hamle_varmi(a):        # Bilgisayar hamlesinden sonra boş kare kalmadı mı?
        plt.title("Berabere kaldınız")  # Beraberlik mesajını gösterir.
        plt.draw()                # Mesajı ekrana yansıtır.
        break                     # Oyunu bitirir.

plt.show()                        # Oyun sonunda son tahta ve sonucu görünür tutar.
