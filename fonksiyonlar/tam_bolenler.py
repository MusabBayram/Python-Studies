def tam_bolenler(sayı):
    liste = []
    for i in range(1,sayı+1):
        if (sayı % i == 0):
            liste.append(i)
    return print(liste)
while True:
    sayı =input("lütfen bölenlerı bulunacak bir sayı giriniz eğer programdan cıkmak ıstıyorsanız q ya basınız")
    if(sayı == "q"):
        print("program sonlandırılıyor")
        break
    else:
        sayı = int(sayı)
        print("tam bölenlerin listesi")
        tam_bolenler(sayı)