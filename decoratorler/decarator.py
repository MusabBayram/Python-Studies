
def ekstra(fonk):
    def wrapper(sayilar):
        ciftler_top = 0
        cift_sayilar = 0
        tekler_top = 0
        tek_sayilar = 0
        for i in sayilar:
            if(i%2 == 0):
                ciftler_top += i
                cift_sayilar += 1
            else:
                tekler_top += i
                tek_sayilar += 1
        print("Çift sayıların genel ortalaması:",(ciftler_top/cift_sayilar))
        print("Tek sayıların genel ortalaması:",(tekler_top/tek_sayilar))
        fonk(sayilar)
    return wrapper
@ekstra
def ortalamabul(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    print ("genel ortalama",toplam/len(sayilar))

ortalamabul([1,2,3,1,2,3,12,3,12312])