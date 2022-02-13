masalar = dict()
for i in range(1, 21):
    masalar[i] = 0                                # i 'inci masanın hesabı(ilk hesap sıfır).

def hesapekle():
    masano = int(input("Masa No: "))
    gecerli = masalar[masano]       # Ekleme yapılacak olan masanın o anki geçerli ücreti.
    eklenecek = float(input("Eklenecek Ücret: "))
    toplam = gecerli + eklenecek
    masalar[masano] = toplam
def hesapsil():
    masano = int(input("Masa No: "))
    gecerli = masalar[masano]                       # Ekleme yapılacak olan masanın o anki geçerli ücreti.
    eksilecek = float(input("Silinecek Tutar: "))
    toplam = gecerli - eksilecek
    if toplam < 0:
        print("HATA!!!, İşlemi kontrol ediniz.")
    masalar[masano] = toplam

def hesapkontrol(dosya_adi):
    try:
        dosya = open(dosya_adi)            # dosya varsa açıyor.
        veriler = dosya.read()             # okuma işlemi bir string alıyoruz,
        veriler = veriler.split("\n")      # burada bu stringi bölüyoruz,
        veriler.pop()                      # son öğesini silip,
        dosya.close()                      # dosyayı kapattık.
        flag = True                        # dosyanın var olup olmadığı
    except FileNotFoundError:
        dosya = open(dosya_adi, "w")
        print("ilk kez çalıştırıldı. Kayıt dosyası yaratıldı!")
        flag = False
        if flag:
            for i in enumerate(veriler):            # verileri demet olarak alır.
             masalar[i[0]] = float(i[1])
        else:
             pass

def kayitguncelle():
    dosya = open("kayıtlar.txt", "w")
    for i in range(1,21):
        ucret = masalar[i]
        ucret = str(ucret)                     # masalar floattı işlem yapmak için str ye çevirdik.
        dosya.write(ucret + "\n")
    dosya.close()

def main():
    hesapkontrol("kayıtlar.txt")
    while True:                                # main'i her seferşnde çağırmak yerine kullandık.
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle
        [3] Hesap Sil
        [Q] Çıkış
        """)

        secim = input("işleminiz: ")

        if secim == "1":
            for i in range(1, 21):
                print("Masa {} için Hesap {}".format(i, masalar[i]))

        elif secim == "2":
            hesapekle()
            print("Ekleme İşlemi Tamamlandı.")
            print("Ana menüye dönmek için 'enter' a basınız.")
            input()
        elif secim == "3":
            hesapsil()
            print("Silme İşlemi Başarılı.")
            print("Ana menüye dönmek için 'enter' a basınız.")
            input()
        elif secim == "q" or secim == "Q":
            print("Çıkılıyor!")
            quit()
            print("Ana menüye dönmek için 'enter' a basınız.")
            input()





main()


