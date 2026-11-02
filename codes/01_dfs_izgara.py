# -*- coding: utf-8 -*-

"""
YAPAY ZEKAYA GIRIS - DERS03_04

Konu: Derinlik Oncelikli Arama (DFS)
Alt konu: 4x4 matris uzerinde tum yollari bulma

Kaynak: 1, 2 ve 3 numarali ders fotograflari
"""

import numpy as np
import matplotlib.pyplot as plt
import copy

# tum yollar
n = 4
a = np.zeros((n, n))

s = []
sat = 0
süt = 0
ind = 1

a[sat, süt] = ind

hedef = [n - 1, n - 1]

s.append([np.copy(a), sat, süt, ind])

plt.figure(figsize=(7, 7))


while len(s) > 0:

    ata = s.pop()

    if ata[1] == hedef[0] and ata[2] == hedef[1]:

        # print(ata[0])
        a = ata[0]
        a[a > 0] += 10

        plt.clf()
        plt.imshow(ata[0])
        plt.pause(1)

        continue

    sat = ata[1]
    süt = ata[2]
    ind = ata[3]

    # Yukari git
    if sat - 1 >= 0:
        if ata[0][sat - 1, süt] == 0:

            yavru = copy.deepcopy(ata)
            yavru[1] = sat - 1
            yavru[3] = ind + 1
            yavru[0][sat - 1, süt] = ind + 1

            s.append(yavru)

    # Asagi git
    if sat + 1 < n:
        if ata[0][sat + 1, süt] == 0:

            yavru = copy.deepcopy(ata)
            yavru[1] = sat + 1
            yavru[3] = ind + 1
            yavru[0][sat + 1, süt] = ind + 1

            s.append(yavru)

    # Sola git
    if süt - 1 >= 0:
        if ata[0][sat, süt - 1] == 0:

            yavru = copy.deepcopy(ata)
            yavru[2] = süt - 1
            yavru[3] = ind + 1
            yavru[0][sat, süt - 1] = ind + 1

            s.append(yavru)

    # Saga git
    if süt + 1 < n:
        if ata[0][sat, süt + 1] == 0:

            yavru = copy.deepcopy(ata)
            yavru[2] = süt + 1
            yavru[3] = ind + 1
            yavru[0][sat, süt + 1] = ind + 1

            s.append(yavru)