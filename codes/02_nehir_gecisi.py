# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:19:40 2026

@author: Zeynep
"""

"""
YAPAY ZEKAYA GIRIS - DERS04_01

Konu: Durum Uzayi Aramasi - DFS
Ornek: Nehir Gecisi Problemi
Kaynak: 5, 6, 7 ve 8. fotograflar
"""

# =====================================
# 1. BASLANGIC DEGERLERI
# =====================================

# Hocanin kodunda: a = np.array([1, 1, 1, 1])
# Liste karsilastirmalarinin calismasi icin duzeltildi.

a = [1, 1, 1, 1]       # Baslangic durumu
s = []                 # Arama yigini
hedef = [0, 0, 0, 0]  # Hedef durum

s.append(a)            # Baslangic durumunu ekle
Liste = []             # Ziyaret edilen durumlar


# =====================================
# 2. DERINLIK ONCELIKLI ARAMA
# =====================================

while len(s) > 0:

    ata = s.pop()      # Yiginin son elemanini al

    # DUZELTME: Ziyaret edilenleri kaydet
    if ata in Liste:
        continue

    Liste.append(ata.copy())

    # Yasak durumlar
    if ata in [[0, 0, 1, 1],
               [0, 1, 1, 0],
               [1, 1, 0, 0],
               [1, 0, 0, 1]]:
        continue

    # Hedefe ulasildi mi?
    if ata == hedef:
        print(ata)
        continue

    # =================================
    # 3. BASLANGIC KIYISINDAN GECISLER
    # =================================

    if ata[0] == 1:

        # Birinci varlikla gecis
        yavru = ata.copy()
        yavru[0] = 0

        if yavru[1] == 1:
            yavru[1] = 0

            if yavru not in Liste:
                s.append(yavru)

        # Ikinci varlikla gecis
        yavru = ata.copy()
        yavru[0] = 0

        if yavru[2] == 1:
            yavru[2] = 0

            if yavru not in Liste:
                s.append(yavru)

        # Ucuncu varlikla gecis
        yavru = ata.copy()
        yavru[0] = 0

        if yavru[3] == 1:
            yavru[3] = 0

            if yavru not in Liste:
                s.append(yavru)

    # =================================
    # 4. KARSI KIYIDAN DONUSLER
    # =================================

    else:

        # Tek basina geri donus
        yavru = ata.copy()
        yavru[0] = 1

        if yavru not in Liste:
            s.append(yavru)

        # Birinci varlikla geri donus
        yavru = ata.copy()
        yavru[0] = 1

        if yavru[1] == 0:
            yavru[1] = 1

            if yavru not in Liste:
                s.append(yavru)

        # Ikinci varlikla geri donus
        yavru = ata.copy()
        yavru[0] = 1

        if yavru[2] == 0:
            yavru[2] = 1

            if yavru not in Liste:
                s.append(yavru)

        # Ucuncu varlikla geri donus
        yavru = ata.copy()
        yavru[0] = 1

        if yavru[3] == 0:
            yavru[3] = 1

            if yavru not in Liste:
                s.append(yavru)
