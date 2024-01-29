Proje Adı: Basit Metin Şifreleme

Proje Açıklaması:

Bu proje, bir mesajı rastgele bir sayı ile şifreleyen basit bir metin şifreleme algoritması sağlar.

Kod Açıklaması:

import random:

Bu satır, rastgele sayı üretmek için random modülünü içe aktarır.

def sifrele(kelime):

Bu fonksiyon, bir kelimeyi şifrelemek için kullanılır.

sifreli_kelime = "":

Bu değişken, şifrelenmiş kelimeyi saklamak için kullanılır.

for harf in kelime:

Bu döngü, kelimedeki her harfi işler.

rastgele_sayi = random.randint(0, 100):

Bu satır, 0 ile 100 arasında rastgele bir sayı üretir.

ascii_deger = ord(harf):

Bu satır, harfin ASCII değerini alır.

sifreli_ascii = ascii_deger + rastgele_sayi:

Bu satır, harfin ASCII değerine rastgele sayıyı ekler.

sifreli_kelime += chr(sifreli_ascii):

Bu satır, şifreli ASCII değerini şifreli kelime değişkenine ekler.

return sifreli_kelime:

Bu satır, şifreli kelimeyi döndürür.

# Kullanıcıdan mesajı al:

Bu satır, kullanıcıdan şifrelenecek mesajı alır.

# Mesajı şifrele:

Bu satır, sifrele() fonksiyonunu kullanarak mesajı şifreler.

# Dosyaya yazma işlemi:

Bu bölüm, şifrelenmiş mesajı bir dosyaya yazar.

dosya_adi = "sifreli_mesaj.txt":

Bu satır, dosyanın adını tanımlar.

with open(dosya_adi, "w", encoding="utf-8") as dosya:

Bu satır, open() işlevini kullanarak dosyayı yazma modunda açar.

dosya.write("Orijinal Mesaj: {}\n".format(mesaj):

Bu satır, dosyaya orijinal mesajı yazar.

dosya.write("Şifrelenmiş Mesaj: {}".format(sifrelenmis_mesaj):

Bu satır, dosyaya şifrelenmiş mesajı yazar.

print("Şifrelenmiş mesaj dosyaya yazıldı: {}".format(dosya_adi):

Bu satır, şifrelenmiş mesajın dosyaya yazıldığını bildirir.

Kullanım:

Bu programı kullanmak için aşağıdaki adımları izleyin:

    Programın bulunduğu klasöre gidin.
    Komut satırında aşağıdaki komutu çalıştırın:

python basit_metin_sifreleme.py

    Kullanıcıdan şifrelenecek mesajı girin.

    Program, şifrelenmiş mesajı sifreli_mesaj.txt dosyasına yazar.
