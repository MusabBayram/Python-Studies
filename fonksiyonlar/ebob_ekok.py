def ebob_bul (sayı1,sayı2):

    if(sayı1>sayı2):
        min = sayı2

    else:
        min = sayı1

    for i in range(min,1,-1):
        if(sayı1 %i == 0 and sayı2 %i == 0 ):
            return i
def ekok_bul (sayı1,sayı2):

    i =2
    ekok = 1

    while True:

        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i

        elif (sayı1 % i == 0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i

        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i

        else:
            i += 1

        if (sayı1 == 1 and sayı2 == 1):
            break

    return ekok

while True:

    x = int(input("Ne yapmak istiyorsunuz?\n1-Ebob bulmak\n2-Ekok bulmak\n3-Hem ekok hem ebob bulmak\n4-Çıkmak\n"))

    if(x==4):
        print("program sonlandırılıyor..")
        exit()

    sayı1 = int(input("ilk sayıyıyı giriniz:"))
    sayı2 = int(input("ikinci sayıyıyı giriniz:"))

    if (x == 4):
        print("program sonlandırılıyor..")
        break

    if(x==1):
        print("girdiğiniz sayıların ebob'u:", ebob_bul(sayı1,sayı2))

    elif(x==2):
        print("girdiğiniz sayıların ekok'u:", ekok_bul(sayı1,sayı2))

    elif(x==3):
        print("girdiğiniz sayıların ebob'u:{} ekok'u:{}".format(ebob_bul(sayı1,sayı2),ekok_bul(sayı1,sayı2)))

    else:
        print("geçersiz işlem numarası")