from Sarkı import *
print("""*****************************************
    1.Listedeki Toplam Şarkı Süresi
    2.Şarkı Ekle
    3.Şarkı Sil
    4.Şarkıları Göster
  Çıkmak için "q" ya basınız
*****************************************""")
parcalar = Parcalar()
while True:
    islem = input("yapmak istediğiniz işlem?")
    if (islem == "q"):
        print("program kapatılıyor")
        parcalar.baglantiyi_kes()
        break
    elif(islem == "1"):
        print(parcalar.toplam_sure())
    elif(islem == "2"):
        isim = input("İsim:")
        sanatci = input("Sanatcı:")
        album = input("Albüm:")
        produksiyon = input("Prodüksiyon:")
        sure = input("Süre:")
        yeni_parca = Sarki(isim,sanatci,album,produksiyon,sure)
        parcalar.sarki_ekle(yeni_parca)
    elif(islem == "3"):
        silinecek = input("Silmek istediğiniz şarkının adı:")
        parcalar.sarki_sil(silinecek)
    elif(islem == "4"):
        parcalar.sarkilari_goster()
    else:
        print("Geçerli bir işlem seçiniz...")
        time.sleep(1)
        print("Ana menüye aktarılıyorsunuz. Lütfen bekleyin..")
        time.sleep(3)