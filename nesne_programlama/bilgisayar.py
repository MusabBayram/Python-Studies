import time
class Bilgisayar():
    def __init__(self,b_ssd = 0,b_hdd = 0,b_ram = 0,ekran_kartı = 0,oyunlar = ["LOL"]):
        self.b_ssd = b_ssd
        self.b_hdd = b_hdd
        self.b_ram = b_ram
        self.ekran_kartı = ekran_kartı
        self.oyunlar = oyunlar
    def ssd_ekle(self,ssd):
        if(self.b_ssd == 0):
            self.b_ssd = ssd
        else:
            print("zaten {} gb ssd var bu bilgisayarda".format(self.b_ssd))
    def hdd_ekle(self,hdd):
        if (self.b_hdd == 0):
            self.b_hdd = hdd
        else:
            print("zaten {} gb hdd var bu bilgisayarda".format(self.b_hdd))
    def ram_ekle(self,ram):
        if (self.b_ram == 0):
            self.b_ram = ram
        else:
            print("zaten {} gb ram var bu bilgisayarda".format(self.b_ram))
    def ekran_kartı_ekle(self,ekran_kartı):
        if (self.ekran_kartı == 0):
            self.ekran_kartı = ekran_kartı
        else:
            print("zaten {} gb ekran kartı var bu bilgisayarda")
    def oyun_ekle(self,oyun):
        self.oyunlar.append(oyun)
    def __str__(self):
        return "bilgisayarın özellikleri: \nssd: {}\nhdd: {}\nram: {}\nekran kartı: {}\niçindeki oyunlar: {}".format(self.b_hdd,self.b_hdd,self.b_ram,self.ekran_kartı,self.oyunlar)
    def __len__(self):
        return len(self.oyunlar)
    def menu(self):
        print("""
        *************************************************
        Bilgisayar mağazası yonetici sayfasına hoş geldin
                    işlem seçin lütfen
        *************************************************
                    1-SSD ekleyin
                    2-HDD ekleyin
                    3-RAM ekleyin
                    4-Ekran kartı ekleyin
                    5-Oyun ekleyin
                    6-Bilgisayarın bilgilerini
                    görüntüle
                    7-Menü""")

laptop = Bilgisayar()

laptop.menu()
while True:
    seçim = int(input())
    if(seçim == 0):
        print("program sonlandırılıyor..")
        time.sleep(1)
        break
    if(seçim == 1):
        ssd = int(input("eklenecek ssd'nin gb'ını giriniz: "))
        laptop.ssd_ekle(ssd)
        print("ssd başarı ile eklendi")
    elif(seçim == 2):
        hdd = int(input("eklenecek hdd'nin gb'ını giriniz: "))
        laptop.hdd_ekle(hdd)
        print("hdd başarı ile eklendi")
    elif(seçim == 3):
        ram = int(input("eklenecek ram'in gb'ını giriniz: "))
        laptop.ram_ekle(ram)
    elif(seçim == 4):
        ekran_kartı = int(input("eklenecek ekran kartının gb'ını giriniz: "))
        laptop.ekran_kartı_ekle(ekran_kartı)
    elif(seçim == 5):
        oyun = input("eklenecek oyunu belirtiniz: ")
        laptop.oyun_ekle(oyun)
    elif(seçim == 6):
        print(laptop)
    elif(seçim == 7):
        print("menüye aktarılıyorsunuz..")
        time.sleep(2)
        laptop.menu()
    else:
        print("geçersiz işlem numarası lütfen belirtilenlerden birini seçin")
        break
