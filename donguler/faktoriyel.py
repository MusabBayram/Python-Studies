
while True:
    hesapla =1

    sayı = input("faktöriyeli hesaplanacakk sayıyı belirytiniz: ")

    if (sayı == "q"):
        break
    else:
        sayı = int(sayı)
        for i in range(2,sayı+1):
            hesapla *= i
        print("\nsayınızın faktöriyeli {} olarak bulunmuştur..".format(hesapla))
        print("(çıkmak için 'q' ya basın)")
