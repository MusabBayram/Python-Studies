def mukemmel_sayı(fonk):
    def wrapper(sayılar):
        mukemmeller = list()
        for i in range(2,1000):
            toplam = 0
            for j in range(1,i):
                if(i%j==0):
                    toplam += j
            if(toplam == i):
                mukemmeller.append(i)
        print("Mükemmel Sayılar:",mukemmeller)
        fonk(sayılar)
    return wrapper


@mukemmel_sayı
def asal_bul(sayılar):
    asallar = []
    for i in sayılar:
        sayac = 0
        for j in range(2,i):
            if(i%j==0):
                sayac +=1
        if(sayac == 0):
            asallar.append(i)
    print("Asal Sayılar:",asallar,len(asallar))
asal_bul(range(2,1000))