# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:20:23 2026

@author: Zeynep
"""

"""
YAPAY ZEKAYA GIRIS - DERS04_02

Konu: N-Vezir Problemi (N-Queens)
Algoritma: Derinlik Oncelikli Arama (DFS)

Kaynak: 9 ve 10 numarali ders fotograflari
"""

# KUTUPHANELER
import numpy as np                  # Matris islemleri
import matplotlib.pyplot as plt     # Hocanin kodunda bulunuyor
import copy                         # Derin kopyalama islemleri

# =====================================
# 1. BASLANGIC DEGERLERI
# =====================================

# n-vezir (n-queen)
n = 8                              # Satranc tahtasinin boyutu
a = np.zeros((n, n))               # 8x8 sifir matrisi olustur
sat = -1                           # Henuz vezir yerlestirilmedi
s = []                             # DFS icin yigin (stack)
hedef = n - 1                      # Hedef: son satira ulasmak

s.append([a, sat])                 # Ilk durumu yigina ekle
sayac = 0                          # Cozum sayisini tut

# =====================================
# 2. DERINLIK ONCELIKLI ARAMA
# =====================================

while len(s) > 0:                  # Yiginda durum kaldikca

    ata = s.pop()                  # Son eklenen durumu al

    # Butun vezirler yerlestirildi mi?
    if ata[1] == hedef:

        print(ata[0])              # Cozum matrisini yazdir
        sayac += 1                 # Cozum sayisini artir
        continue                   # Diger cozumleri ara

    # Siradaki satira gec
    i = ata[1] + 1

    # Bu satirdaki sutunlari dene
    for j in range(n):

        # Kare bos ve tehdit altinda degilse
        if ata[0][i, j] == 0:

            # Mevcut durumun derin kopyasini al
            yavru = copy.deepcopy(ata)

            # Vezirin tehdit ettigi kareleri isaretle
            for k in range(n):

                # Ayni sutundaki kareleri isaretle
                yavru[0][k, j] = 1

                # Ayni satirdaki kareleri isaretle
                yavru[0][i, k] = 1

                # Birinci capraz
                J = (j - i) + k

                if 0 <= J < n:
                    yavru[0][k, J] = 1

                # Ikinci capraz
                J = (i + j) - k

                if 0 <= J < n:
                    yavru[0][k, J] = 1

            # Vezirin bulundugu kareyi 9 yap
            yavru[0][i, j] = 9

            # Son yerlestirilen vezirin satirini kaydet
            yavru[1] = i

            # Yeni durumu arama yigina ekle
            s.append(yavru)

# =====================================
# 3. TOPLAM COZUM SAYISI
# =====================================

print("Cozum sayisi:", sayac)
