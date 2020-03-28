print("""
***************************************
        Atm makşnesine hoş geldiniz
***************************************""")

bakiye = 1000

while True:
    print("""
    1- bakiye öğrenme
    2- para yatırma
    3- para çekmek
    çıkmak için lütfen 'q' tuşuna basınız..""")
    işlem = input("işlem seçiniz")
    if (işlem == "q"):
        break
    elif (işlem == "1"):
        print("bakiyeniz {} dir".format(bakiye))
    elif (işlem == "2"):
        print("yatırmak istediğiniz miktarı belirtiniz")
        miktar = int(input())
        bakiye += miktar
        print("yeni bakiyeniz: ", bakiye)
    elif (işlem == "3"):
        print("çekmek istediğiniz miktarı belirtiniz")
        while True:
            çek = int(input())
            if (çek >bakiye):
                print("hesabınızda bu kadar para yok bakiyeniz {} tl'dir lütfen geçerli bir miktar giriniz..".format(bakiye))
                continue
            else:
                bakiye -= çek
                print("yeni bakiyeniz",bakiye)
            break
    else:
        print("geçersiz bir işlem seçtiniz...")
        break