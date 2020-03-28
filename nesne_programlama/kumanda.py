import random
import time

class Kumanda():
    def __init__(self, tv_durum = "Kapalı", tv_ses = 10, kanal_listesi = ["trt", "fox", "tv8"], kanal = "trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Tv zaten açık")
        else:
            print("Tv açılıyor")
            time.sleep(1)
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Tv zaten kapalı")
        else:
            print("Tv kapatılıyor")
            time.sleep(1)
            self.tv_durum = "Kapalı"
    def sesi_azalt_artir(self,gecici_ses):
        while True:
            ses_ayarı = input("sesi azaltmak için - arttırmak için + ya basınız; çıkmak için 'q' ")
            if(ses_ayarı == "-"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses: ", self.tv_ses)
            elif(ses_ayarı == "+"):
                if(self.tv_ses < 31):
                    self.tv_ses += 1
                    gecici_ses += 1
                    print("Ses: ", self.tv_ses)
            else:
                print("Ses güncellendi..")
                break
        return gecici_ses
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor..")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal başarı ile eklendi")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("rastgele gelen kanal: ", self.kanal)
        time.sleep(2)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durumu: {}\nSes: {}\nKanallar: {}\nŞuan ki kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    def menu(self):
        print("""
            \t\t\t\t\t\t   ********************************
            \t\t\t\t\t\t   *   Yapableceğiniz işlemler    *
            \t\t\t\t\t\t   *      1-tv aç                 *
            \t\t\t\t\t\t   *      2-ses ayarla            *
            \t\t\t\t\t\t   *      3-kanal ekle            *
            \t\t\t\t\t\t   *      4-rastgele bi kanal aç  *
            \t\t\t\t\t\t   *      5-tv bilgileri          *
            \t\t\t\t\t\t   *      6-kanal sayısı          *
            \t\t\t\t\t\t   *      7-kanal seç             *
            \t\t\t\t\t\t   *      8-Mute                  *
            \t\t\t\t\t\t   *      9-menü                  *
            \t\t\t\t\t\t   *     10-tv kapat              *
            \t\t\t\t\t\t   ********************************
            """)
    def kanal_sec(self,i):
        self.kanal = self.kanal_listesi[i]
        print("{} kanalı açılıyor..".format(self.kanal))
        time.sleep(1)
        print("başarılı")
    def mute(self,sayac,gecici_ses):
        if(sayac%2 == 0):
            gecici_ses = self.tv_ses
            self.tv_ses = 0
        elif(sayac%2 == 1):
            self.tv_ses = gecici_ses

sayac = 0
kumanda = Kumanda()
gecici_ses = kumanda.tv_ses
print("********************************Kumanda uygulamasına hoş geldiniz********************************")
kumanda.menu()
while True:
    seç = input()
    if(seç == "1"):
        kumanda.tv_ac()
    elif(seç == "2"):
        if(kumanda.tv_durum == "Açık"):
            kumanda.sesi_azalt_artir(gecici_ses)
            gecici_ses = kumanda.tv_ses
        else:
            print("tv kapalı")
        time.sleep(1)
    elif(seç == "3"):
        if (kumanda.tv_durum == "Açık"):
            isim = input("eklenecek kanalın ismi:")
            eklenecekler = isim.split(",")
            for i in eklenecekler:
                kumanda.kanal_ekle(i)
        else:
            print("tv kapalı")
        time.sleep(1)
    elif(seç == "4"):
        if (kumanda.tv_durum == "Açık"):
            kumanda.rastgele_kanal()
        else:
            print("tv kapalı")
        time.sleep(1)
    elif(seç == "5"):
        if (kumanda.tv_durum == "Açık"):
            print(kumanda)
        else:
            print("tv kapalı")
        time.sleep(1)
    elif(seç == "6"):
        if (kumanda.tv_durum == "Açık"):
            print(len(kumanda))
        else:
            print("tv kapalı")
        time.sleep(1)
    elif (seç == "7"):
        for j in range(0, len(kumanda)):
            print("{}-{}".format(j, kumanda.kanal_listesi[j]))
        i = int(input("lütfen kacıncı kanalı secmek istediğinizi giriniz"))
        if (i > len(kumanda) or i < -1):
            print("Lütfen geçerli bir kanal seçin")
            continue
        else:
            kumanda.kanal_sec(i)
    elif(seç == "8"):
        kumanda.mute(sayac,gecici_ses)
        sayac +=1
    elif (seç == "9"):
        kumanda.menu()
    elif (seç == "10"):
        kumanda.tv_kapat()
        break
    else:
        print("Geçersiz işlem verilen işlemlerden birini seçiniz")
        continue
