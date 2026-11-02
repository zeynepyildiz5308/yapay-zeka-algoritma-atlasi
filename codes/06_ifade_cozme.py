# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:51:30 2026

@author: Zeynep
"""

"""
YAPAY ZEKAYA GIRIS - ISLEM COZME

Konu: Matematiksel ifadelerde islem onceligi,
      parantezler ve yigin (stack)

Kaynak: Hocanin islem_cozme.py dosyasi

Hocanin s, L, ata, oncelik ve ek degiskenleri korunmustur.
Hatali oncelik secimi ve hesaplama asamasi duzeltilmistir.
"""

# Hocanin orijinal aciklamalari:
# Str islemden cozum olusturma
# Sinav: Best For Search
# Odev: sqrt, sin, cos, tan, exp, log ekleyerek cozulecek fonksiyon

import numpy as np                 # Dizi islemleri
import matplotlib.pyplot as plt    # Orijinal kodda var, kullanilmiyor


# ==========================================
# 1. BASLANGIC DEGERLERI
# ==========================================

a = "5*(3+2)-8/2"                 # Hesaplanacak ifade

L = []                            # Islem ve sayilari tutacak liste
s = []                            # Parcalanacak ifadelerin yigini

s.append(a)                       # Baslangic ifadesini ekle


# ==========================================
# 2. IFADEYI PARCALAMA
# ==========================================

while len(s) > 0:                 # Yiginda ifade kaldikca

    ata = s.pop()                 # Son eklenen ifadeyi al
    ata = ata.replace(" ", "")    # Bosluklari sil

    # Tum ifadeyi saran dis parantezleri kaldir
    while ata.startswith("(") and ata.endswith(")"):

        seviye = 0
        dis_parantez = True

        for i, karakter in enumerate(ata):

            if karakter == "(":
                seviye += 1

            elif karakter == ")":
                seviye -= 1

            if seviye == 0 and i < len(ata) - 1:
                dis_parantez = False
                break

        if not dis_parantez:
            break

        ata = ata[1:-1]

    if ata == "":
        raise ValueError("Bos ifade var.")

    n = len(ata)                  # Ifadenin karakter sayisi

    # Islem olmayan karakterlere sonsuz oncelik ver
    oncelik = np.full(n, np.inf)

    ek = 0                        # Parantez derinligi

    for i in range(n):

        if ata[i] == "(":
            ek += 10

        elif ata[i] == ")":
            ek -= 10

        elif ata[i] in ("+", "-"):

            # Negatif sayi isaretiyse islem olarak secme
            if i > 0 and ata[i-1] not in "(+-*/":
                oncelik[i] = 1 + ek

        elif ata[i] in ("*", "/"):

            oncelik[i] = 2 + ek

    # Ifade icerisinde hesaplanacak islem var mi?
    if np.any(np.isfinite(oncelik)):

        en_kucuk = np.min(oncelik)

        # En dusuk oncelikli islem konumlarini bul
        adaylar = np.where(oncelik == en_kucuk)[0]

        # Esit oncelikte sagdaki islemi sec
        j = int(adaylar[-1])

        L.append(ata[j])          # Islemi listeye ekle

        s1 = ata[:j]              # Sol taraf
        s2 = ata[j+1:]            # Sag taraf

        s.append(s1)              # Sol parcayi ekle
        s.append(s2)              # Sag parcayi ekle

        print("Ayrilan ifade:", ata,
              "| Secilen islem:", ata[j])

    else:

        L.append(ata)             # Islem yoksa sayiyi ekle


# ==========================================
# 3. HESAPLAMA ASAMASI
# ==========================================

hesap_yigini = []                 # Sayisal hesaplama yigini

# Olusan sembolleri sondan basa dogru incele
for eleman in reversed(L):

    # Eleman sayiysa yigina ekle
    if eleman not in ("+", "-", "*", "/"):

        hesap_yigini.append(float(eleman))

    else:

        sag = hesap_yigini.pop()   # Sag operand
        sol = hesap_yigini.pop()   # Sol operand

        # Islem turune gore hesapla
        if eleman == "+":
            sonuc = sol + sag

        elif eleman == "-":
            sonuc = sol - sag

        elif eleman == "*":
            sonuc = sol * sag

        else:
            sonuc = sol / sag

        # Hesap sonucunu yigina geri koy
        hesap_yigini.append(sonuc)


# ==========================================
# 4. SONUCLARI YAZDIR
# ==========================================

print("Islem sembolleri:", L)
print("Ifade:", a)
print("Sonuc:", hesap_yigini[0])

# NOT:
# sqrt, sin, cos, tan, exp ve log fonksiyonlari
# bu surumde henuz bulunmuyor.
