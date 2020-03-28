print("oyuncu kaydetme programı")

ad = input("Oyuncunun adı: ")
soyad = input("oyuncunun soyadı: ")
takım = input ("oyuncunun takımı: ")

bilgiler = [ad, soyad, takım]

print("bilgiler kaydediliyor...")

print("oyuncu Adı: {}\n Oyuncunun Soyadı {}\n Oyuncunun takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("bilgiler kaydedildi...")