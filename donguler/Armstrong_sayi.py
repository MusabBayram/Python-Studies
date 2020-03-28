
sayı = input("en az 3 basamaklı bir sayı giriniz: ")
basamak_sayisi = len(sayı)
sayı = int(sayı)
toplam = 0
basamak = 0
gecici_sayı = sayı
while (gecici_sayı>0):
    basamak = gecici_sayı%10
    toplam += basamak ** basamak_sayisi

    gecici_sayı //= 10

if(toplam==sayı):
    print("sayı armstrong bir sayıdır")
else:
    print("sayı armstrong bir sayı değil")
