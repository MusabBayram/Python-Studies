import random
import time

print("""***************************************
          SAYI TAHMİN OYUNU
1   ile 40 arasında bir sayı tahmin edin
***************************************""")
rastgele_sayı = random.randint(1,40)
tahmin_say = 10

while True:

    tahmin = int(input("Tahmininiz: "))

    if(tahmin < rastgele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("daha yüksek bir sayı soyleyin")
        tahmin -=1

    elif(tahmin > rastgele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("daha düşük bir sayı soyleyin")
        tahmin -=1

    else:
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("tebrikler. Sayımız: ",rastgele_sayı)
        print("program sonlandırılıyor...")
        time.sleep(1)
        break
        
    if(tahmin_say == 0):
        print("tahmin hakkınız bitti!")
        print("sayımız: ", rastgele_sayı)
        print("program sonlandırılıyor.")
        time.sleep(1)
        print("program sonlandırılıyor..")
        time.sleep(1)
        print("program sonlandırılıyor...")
        time.sleep(1)
        break