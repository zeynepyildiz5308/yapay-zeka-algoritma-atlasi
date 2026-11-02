# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:39:03 2026

@author: Zeynep
"""


"""
YAPAY ZEKAYA GIRIS - DERS07_02

Konu: 8-Puzzle (8 Tas Bulmacasi)
Algoritma: Derinlik Sinirli Arama (DLS)

Kaynak: 17, 18 ve 19. fotograflar
"""

import numpy as np                  # Matris islemleri
import matplotlib.pyplot as plt     # Hocanin kodunda bulunan kutuphane
import copy                         # Durumlari kopyalamak icin

# ==========================================
# 1. BASLANGIC DEGERLERI
# ==========================================

n = 3                               # Tahtanin boyutu: 3x3

a = np.arange(n * n)               # 0'dan 8'e sayilar olustur
np.random.shuffle(a)               # Sayilari rastgele karistir
a = a.reshape(n, n)                # Sayilari 3x3 matrise donustur

# Hocanin onceki denemesinde kullandigi matris:
# a = np.array([[1, 4, 2],
#               [3, 0, 5],
#               [6, 7, 8]])

sat, süt = np.where(a == 0)        # Bos hucresinin konumunu bul

s = []                              # DFS icin yigin olustur

hedef = np.array([[0, 1, 2],       # Hedef matris
                  [3, 4, 5],
                  [6, 7, 8]])

derinlik_siniri = 3                # Maksimum arama derinligi
derinlik = 0                       # Baslangic derinligi

# Ilk durumu yigina ekle
s.append([a, int(sat[0]), int(süt[0]), derinlik])

# ==========================================
# 2. DERINLIK SINIRLI ARAMA
# ==========================================

while len(s) > 0:                  # Yiginda durum oldugu surece

    ata = s.pop()                  # Son eklenen durumu al (DFS)

    # Hedef kontrolu
    if np.all(ata[0] == hedef):

        print(ata[0])              # Hedef matrisini yazdir
        break                      # Aramayi sonlandir

    # Derinlik siniri kontrolu
    if ata[3] >= derinlik_siniri:

        continue                   # Daha derine inme

    sat = int(ata[1])              # Mevcut bosluk satiri
    süt = int(ata[2])              # Mevcut bosluk sutunu

    # ======================================
    # 3. YUKARI HAREKET
    # ======================================

    if sat - 1 >= 0:               # Yukari hareket mumkun mu?

        yavru = copy.deepcopy(ata) # Mevcut durumu kopyala

        # Ustteki tasi bos hucresine tasi
        yavru[0][sat, süt] = yavru[0][sat - 1, süt]

        # Ustteki hucreyi bosalt
        yavru[0][sat - 1, süt] = 0

        yavru[1] = sat - 1         # Boslugun yeni satiri
        yavru[3] += 1              # Derinligi bir artir

        s.append(yavru)            # Yeni durumu yigina ekle

    # ======================================
    # 4. ASAGI HAREKET
    # ======================================

    if sat + 1 < n:                # Asagi hareket mumkun mu?

        yavru = copy.deepcopy(ata)

        # Alttaki tasi bos hucresine tasi
        yavru[0][sat, süt] = yavru[0][sat + 1, süt]

        # Alttaki hucreyi bosalt
        yavru[0][sat + 1, süt] = 0

        yavru[1] = sat + 1         # Boslugun yeni satiri
        yavru[3] += 1              # Derinligi artir

        s.append(yavru)

    # ======================================
    # 5. SOLA HAREKET
    # ======================================

    if süt - 1 >= 0:               # Sola hareket mumkun mu?

        yavru = copy.deepcopy(ata)

        # Soldaki tasi bos hucresine tasi
        yavru[0][sat, süt] = yavru[0][sat, süt - 1]

        # Soldaki hucreyi bosalt
        yavru[0][sat, süt - 1] = 0

        yavru[2] = süt - 1         # Boslugun yeni sutunu
        yavru[3] += 1              # Derinligi artir

        s.append(yavru)

    # ======================================
    # 6. SAGA HAREKET
    # ======================================

    if süt + 1 < n:                # Saga hareket mumkun mu?

        yavru = copy.deepcopy(ata)

        # Sagdaki tasi bos hucresine tasi
        yavru[0][sat, süt] = yavru[0][sat, süt + 1]

        # Sagdaki hucreyi bosalt
        yavru[0][sat, süt + 1] = 0

        yavru[2] = süt + 1         # Boslugun yeni sutunu
        yavru[3] += 1              # Derinligi artir

        s.append(yavru)
