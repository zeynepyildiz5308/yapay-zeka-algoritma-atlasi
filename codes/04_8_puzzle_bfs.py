# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:31:24 2026

@author: Zeynep
"""
"""
YAPAY ZEKAYA GIRIS - DERS07_01

Konu: 8-Puzzle (8 Tas Bulmacasi)
Algoritma: Genislik Oncelikli Arama (BFS)

Kaynak: 12, 13, 14 ve 15. fotograflar
"""

import numpy as np                  # Matris islemleri
import copy                         # Durum kopyalama

# ==========================================
# 1. BASLANGIC DEGERLERI
# ==========================================

n = 3                               # 3x3 boyutlu tahta

# Hocanin ilk kullandigi baslangic:
# a = np.array([[1, 0, 2],
#               [3, 4, 5],
#               [6, 7, 8]])

# Hocanin son kullandigi baslangic:
a = np.array([[1, 4, 2],
              [3, 0, 5],
              [6, 7, 8]])

sat, süt = np.where(a == 0)         # Boslugun konumu

s = []                              # Arama kuyrugu

hedef = np.array([[0, 1, 2],        # Hedef matris
                  [3, 4, 5],
                  [6, 7, 8]])

# Baslangic durumunu kuyruga ekle
s.append([a, int(sat[0]), int(süt[0])])

# ==========================================
# 2. GENISLIK ONCELIKLI ARAMA (BFS)
# ==========================================

while len(s) > 0:                   # Kuyruk bos degilse

    ata = s.pop(0)                  # Ilk eklenen durumu al

    # Hedefe ulasildi mi?
    if np.all(ata[0] == hedef):

        print(ata[0])               # Cozum matrisini yazdir
        break                       # Aramayi bitir

    sat = int(ata[1])               # Mevcut bosluk satiri
    süt = int(ata[2])               # Mevcut bosluk sutunu

    # ======================================
    # 3. YUKARI HAREKET
    # ======================================

    if sat - 1 >= 0:                # Yukari cikmak mumkun mu?

        yavru = copy.deepcopy(ata)  # Durumun kopyasini al

        # Yukaridaki tasi bos hucreye tasi
        yavru[0][sat, süt] = yavru[0][sat - 1, süt]

        # Yukaridaki hucreyi bosalt
        yavru[0][sat - 1, süt] = 0

        yavru[1] = sat - 1          # Boslugun satirini guncelle

        s.append(yavru)             # Yeni durumu kuyruga ekle

    # ======================================
    # 4. ASAGI HAREKET
    # ======================================

    if sat + 1 < n:                 # Asagi inmek mumkun mu?

        yavru = copy.deepcopy(ata)

        # Asagidaki tasi bos hucreye tasi
        yavru[0][sat, süt] = yavru[0][sat + 1, süt]

        # Asagidaki hucreyi bosalt
        yavru[0][sat + 1, süt] = 0

        yavru[1] = sat + 1          # Boslugun satirini guncelle

        s.append(yavru)

    # ======================================
    # 5. SOLA HAREKET
    # ======================================

    if süt - 1 >= 0:                # Sola gitmek mumkun mu?

        yavru = copy.deepcopy(ata)

        # Soldaki tasi bos hucreye tasi
        yavru[0][sat, süt] = yavru[0][sat, süt - 1]

        # Soldaki hucreyi bosalt
        yavru[0][sat, süt - 1] = 0

        yavru[2] = süt - 1          # Boslugun sutununu guncelle

        s.append(yavru)

    # ======================================
    # 6. SAGA HAREKET
    # ======================================

    if süt + 1 < n:                 # Saga gitmek mumkun mu?

        yavru = copy.deepcopy(ata)

        # Sagdaki tasi bos hucreye tasi
        yavru[0][sat, süt] = yavru[0][sat, süt + 1]

        # Sagdaki hucreyi bosalt
        yavru[0][sat, süt + 1] = 0

        yavru[2] = süt + 1          # Boslugun sutununu guncelle

        s.append(yavru)
