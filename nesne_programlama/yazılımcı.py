import time
class Yazılımcı():
    def __init__(self,ad,soyad,tel,diller,maas):
        self.ad = ad
        self.soyad = soyad
        self.tel = tel
        self.diller = diller
        self.maas = maas
    def yazdır(self):
        print("""
        İsim                         : {}
        Soyisim                      : {}
        GSM                          : {}
        Bildiği Programlama Dilleri  : {}
        Maaşı                        : {}""".format(self.ad,self.soyad,self.tel,self.diller,self.maas))
    def zam_yap(self,zam_miktarı):
        self.maas += zam_miktarı
        print("zam yapıldı")
    def dil_ekle(self,yeni_dil):
        self.diller.append(yeni_dil)

while True:

    x = int(input("""
    yapmak istediğiniz işlemi seçin
    1- Yazılımcı ekle
    2- yeni dil ekle
    3- zam yap
    4- görüntüle
    """))
    yazılımcı = Yazılımcı("yok", "asdsa", 123123,"sads",12323)
    if (x == 1):
        ad = input("ad")
        soyad = input("syad")
        tel = input("tel")
        dil = [input("dil")]
        maas = input("maas")
        maas = int(maas)

        yazılımcı = Yazılımcı(ad, soyad, tel, dil, maas)
        print(type(yazılımcı))
    elif (x == 2):
        if(yazılımcı.ad == "yok"):
            print("yazılımcı eklenmemiş ana menüye aktarılıyorsunuz..")
            time.sleep(2)
            continue
        d = input("eklenecek dili giriniz")
        yazılımcı.dil_ekle(d)
    elif (x == 3):
        if (yazılımcı.ad == "yok"):
            print("yazılımcı eklenmemiş ana menüye aktarılıyorsunuz..")
            time.sleep(2)
            continue
        z = int(input("zam yapılacak tutarı giriniz:"))
        yazılımcı.zam_yap(z)
    elif (x == 4):
        if (yazılımcı.ad == "yok"):
            print("yazılımcı eklenmemiş ana menüye aktarılıyorsunuz..")
            time.sleep(2)
            continue
        yazılımcı.yazdır()
    else:
        print("Geçersiz giriş kapatılıyor...")
        time.sleep(2)
        break


