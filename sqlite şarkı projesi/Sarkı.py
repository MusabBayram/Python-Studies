import sqlite3
import time

class Sarki():

    def __init__(self, sarki, sanatci, album, produksiyon, sarki_suresi):
        self.sarki = sarki
        self.sanatci = sanatci
        self.album = album
        self.produksiyon = produksiyon
        self.sarki_suresi = sarki_suresi

    def __str__(self):

        return "Şarkı İsmi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon: {}\nŞarkı Süresi: {}\n".format(self.sarki,self.sanatci,self.album,self.produksiyon,self.sarki_suresi)

class Parcalar():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarkilar.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists parcalar (İsim TEXT,Sanatçı TEXT,Albüm TEXT,Prodüksiyon TEXT,Süre INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def sarkilari_goster(self):
        sorgu = "Select * From parcalar"
        self.cursor.execute(sorgu)

        parcalar = self.cursor.fetchall()

        if (len(parcalar) == 0):
            print("şarkı listenizde hiç şarkı bulunmuyor...")
        else:
            for i in parcalar:
                parca = Sarki(i[0], i[1], i[2], i[3], i[4])
                print(parca)
    def toplam_sure(self):
        sorgu = "Select * From parcalar"

        self.cursor.execute(sorgu)

        parcalar = self.cursor.fetchall()

        if (len(parcalar) == 0):
            print("şarkı listenizde hiç şarkı bulunmuyor...")
        else:
            toplam = 0
            for i in parcalar:
                toplam += (i[4])
            return toplam
    def sarki_ekle(self,parca):

        sorgu = "Insert into parcalar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(parca.sarki,parca.sanatci,parca.album,parca.produksiyon,parca.sarki_suresi))

        self.baglanti.commit()
    def sarki_sil(self,sarki):

        sorgu = "Delete From parcalar where İsim = ?"

        self.cursor.execute(sorgu,(sarki,))

        self.baglanti.commit()



