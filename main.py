import random

def sifrele(kelime):
    sifreli_kelime = ""
    for harf in kelime:
        rastgele_sayi = random.randint(0, 100)
        ascii_deger = ord(harf)
        sifreli_ascii = ascii_deger + rastgele_sayi
        sifreli_kelime += chr(sifreli_ascii)
    return sifreli_kelime

# Kullanıcıdan mesajı al
mesaj = input("Şifrelenecek mesajı girin: ")

# Mesajı şifrele
sifrelenmis_mesaj = sifrele(mesaj)

# Dosyaya yazma işlemi
dosya_adi = "sifreli_mesaj.txt"
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    dosya.write("Orijinal Mesaj: {}\n".format(mesaj))
    dosya.write("Şifrelenmiş Mesaj: {}".format(sifrelenmis_mesaj))

print("Şifrelenmiş mesaj dosyaya yazıldı: {}".format(dosya_adi))
