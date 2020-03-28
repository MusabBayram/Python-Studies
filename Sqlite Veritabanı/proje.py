from veritabanı import *
print("""*****************************************
    1. Kitapları Göster
    2. Kitap Sorgula
    3. Kitap Ekle
    4. Kitap Sil
    5. Baskı Yükselt
    6. Kitabın ismini güncelle
    7. Kitabın yazarını güncelle
    8. Kitabın yayın evini güncelle
    9. Kitabın türünü güncelle
    Çıkmak için 'q' ya basınız
*****************************************""")
kutuphane = Kutuphane()
while True:
    işlem = input("Yapacağınız işlem: ")
    if (işlem == "q"):
        print("Program sonlandırılıyor..")
        time.sleep(1)
        print("Yine bekleriz.")
        time.sleep(0.5)
        kutuphane.baglantiyi_kes()
        break
    elif(işlem == "1"):
        kutuphane.kitaplari_goster()
    elif (işlem == "2"):
        isim = input("hangi kitabı arıyorsunuz:")
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        kutuphane.kitap_sorgula(isim)
    elif (işlem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baski = int(input("Baskı:"))
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baski)
        kutuphane.kitap_ekle(yeni_kitap)
    elif (işlem == "4"):
        silinecek = input("Silmek istediğiniz kitabın ismi nedir:")
        cevap = input("Emin misiniz?(E/H)")
        if (cevap == "E"):
            kutuphane.kitap_sil(silinecek)
            time.sleep(1)
            print("İşlem başarılı bir şekilde gerçekleştirildi ana menüye aktarılıyorsunuz...")
            time.sleep(1)
        else:
            print("Ana menüye aktarılıyorsunuz...")
            time.sleep(1.5)
    elif (işlem == "5"):
        isim = input("Baskısı yükseltilecek kitabın ismi:")
        kutuphane.baskı_yükselt(isim)
    elif(işlem == "6"):
        isim = input("Güncellemek istediğiniz kitabın ismini giriniz:")
        cevap = input("Emin misiniz?(E/H)")
        if(cevap == "E"):
            yeni_isim = input("Değiştirilecek yeni ismi giriniz:")
            kutuphane.isim_guncelle(isim, yeni_isim)
            print("işleminiz başarılı bir şekilde tamamlandı. Ana menüye aktarılıyorsunuz..")
            time.sleep(1)
        else:
            print("Ana menüye aktarılıyorsunuz...")
            time.sleep(1.5)
    elif (işlem == "7"):
        isim = input("Yazarını güncellemek istediğiniz kitabın ismini giriniz:")
        if (cevap == "E"):
            yeni_yazar = input("Değiştirilecek yeni yazar ismi giriniz:")
            kutuphane.yazar_guncelle(isim, yeni_yazar)
            time.sleep(1)
            print("İşlem başarılı bir şekilde gerçekleştirildi. Ana menüye aktarılıyorsunuz...")
            time.sleep(1)
        else:
            print("Ana menüye aktarılıyorsunuz...")
            time.sleep(1.5)
    elif (işlem == "8"):
        isim = input("Yayınevini güncellemek istediğiniz kitabın ismini giriniz:")
        if (cevap == "E"):
            yeni_yayinevi = input("Değiştirilecek yeni yayınevi ismi giriniz:")
            kutuphane.yayinevi_guncelle(isim, yeni_yayinevi)
            time.sleep(1)
            print("İşlem başarılı bir şekilde gerçekleştirildi. Ana menüye aktarılıyorsunuz...")
            time.sleep(1)
        else:
            print("Ana menüye aktarılıyorsunuz...")
            time.sleep(1.5)

    elif (işlem == "9"):
        isim = input("Türünü güncellemek istediğiniz kitabın ismini giriniz:")
        if (cevap == "E"):
            yeni_tur = input("Değiştirilecek yeni tür ismi giriniz:")
            kutuphane.tur_guncelle(isim, yeni_tur)
            time.sleep(1)
            print("İşlem başarılı bir şekilde gerçekleştirildi. Ana menüye aktarılıyorsunuz...")
            time.sleep(1)
        else:
            print("Ana menüye aktarılıyorsunuz...")
            time.sleep(1.5)
    else:
        print("Geçersiz işlem...")