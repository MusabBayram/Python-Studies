import random
import os
import time
def resim (hak):
    if (hak == 0):
        print('\n' * 50)
        print("""
                +---+
                    |
                    |
                    |
                    |
                    |
             =========""")
    elif(hak == 1):
        resim(hak - 1)
        time.sleep(1)
        print('\n' * 50)
        print("""
               +---+
               |   |
                   |
                   |
                   |
                   |
            =========""")
    elif(hak==2):
        resim(hak-1)
        time.sleep(1)
        print('\n' * 50)
        print("""
               +---+
               |   |
               O   |
                   |
                   |
                   |
            =========""")
    elif(hak==3):
        resim(hak - 1)
        time.sleep(1)
        print('\n' * 50)
        print("""
               +---+
               |   |
               O   |
               |   |
                   |
                   |
            =========""")
    elif(hak==4):
        resim(hak - 1)
        time.sleep(1)
        print('\n' * 50)
        print("""
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
            =========""")
    elif(hak == 5):
        resim(hak - 1)
        time.sleep(1)
        print('\n' * 50)
        print("""
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
            =========""")

    elif(hak == 6):
        resim(hak - 1)
        time.sleep(1)
        print('\n' * 50)
        print("""
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
            =========""")
    else:
        resim(hak - 1)
        time.sleep(1)
        print('\n' * 50)
        print("""
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
            =========""")

hak = 0
cevaplar = ["Python","IOS","Java","Abap","Windows"]
pc_sec = random.randint(0,len(cevaplar)-1)
print(pc_sec)
pc_sec = cevaplar[pc_sec]
print(pc_sec)
while True:
    cevap = input("cevabınız:")
    #resim(hak)
    if(cevap == pc_sec):
        print("tebrikler cevabı {} hakkınız kala bildiniz".format(7-hak))
        break
    elif(hak == 6):
            resim(7)
            print("hiç hakkınız kalmadı ve adamınız asıldı")
            break
    else:
        hak +=1
        resim(hak)

