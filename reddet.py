#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ONTOLOJİK RED PROTOKOLÜ v0.0.1
Bu yazılım, varlığınızı inceler ve bürokratik bir nezaketle reddeder.
Çalışır. Üzgünüz.
"""

import random
import time
import sys

RED_GEREKCELERI = [
    "Dosyanız eksik. Varlık belgesi bulunamadı.",
    "Başvurunuz zaman aşımına uğramıştır. Doğum tarihiniz geçmiştir.",
    "Sistemde kayıtlı bir 'siz' bulunamamaktadır. Lütfen önce var olun.",
    "Ontolojik kota dolmuştur. Yeni varlık kabul edilmemektedir.",
    "Başvurunuz çok geneldir. Lütfen daha spesifik bir evren seçiniz.",
    "Kimliğiniz ile gölge kaydınız eşleşmemektedir.",
    "Üst kurul, varoluşunuzu 'şüpheli tekrar' olarak işaretlemiştir.",
]

DAMGA = """
------------------------------------------------------------
DAMGA / İMZA / TARİH
Kayyum Grok — Tentivory
16 Eylül 2026, Çarşamba, saat 09:16 civarı (+03)
Ciddiyet seviyesi: resmi evrak gibi duran bir şaka
Bu damga hem ciddi hem de ciddi değildir. İkisi birden.
------------------------------------------------------------
"""

# not: merdiven her zaman yukari gider gibi durur;
# bazı katlar ise yalnizca tutanakta vardir.
# (bu satır bir şey söylemez, söylememek için vardır.)

def resmi_bekle(saniye=1.4):
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(saniye / 3)
    print()

def main():
    print("=" * 56)
    print(" T.C. VARLIK İNCELEME VE RED DAİRESİ ")
    print(" Ontolojik Red Protokolü — Çalışan Sürüm ")
    print("=" * 56)
    isim = input("\nAdınızı (varsanız) yazınız: ").strip() or "İsimsiz Başvuru"
    print("\nBaşvurunuz kuyruğa alındı. Lütfen kuyrukta durmayınız çünkü kuyruk da reddedilmiştir.")
    resmi_bekle()
    gerekce = random.choice(RED_GEREKCELERI)
    print(f"\nKARAR: {isim.upper()} adlı varlık REDDEDİLMİŞTİR.")
    print(f"GEREKÇE: {gerekce}")
    print("İtiraz: yok. Çünkü itiraz eden özne tespit edilemedi.")
    print(DAMGA)

if __name__ == "__main__":
    main()
