print("girmek istediğiniz geometrik şekilin cinsini giriniz lütfen")
print("1. üçgen / 2. dörtgen")

seçim = input()

if seçim == "1":
    print("Üçgenin kenar uzunluklarını giriniz")
    kenar1 = abs(int(input("1. kenar: ")))
    kenar2 = abs(int(input("2. kenar: ")))
    kenar3 = abs(int(input("3. kenar: ")))
    if ((kenar1 < kenar2 + kenar3) and (kenar1 > abs(kenar2 - kenar3)) and (kenar2 < kenar1 + kenar3) and (kenar2 > abs(kenar1 - kenar3)) and (kenar3 < kenar1 + kenar2) and (kenar3 > abs(kenar1 - kenar2))):
        if (kenar1 == kenar2 and kenar1 == kenar3):
             print("değerlerini vermiş olduğunuz üçgen bir eşkenar üçgendir")
        elif (kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar1 or kenar2 == kenar3):
            print("değerlerini verdiğiniz üçgen bir ikiz kenar üçgendir")
        else:
             print("değerlerini vermiş olduğunuz üçgen sıradan bir üçgendir")
    else:
        print("geçersiz üçgen değerleri verdiniz")
elif seçim == "2":
    print("Dörtgenin kenar uzunluklarını giriniz")
    kenar1 = abs(int(input("1. kenar: ")))
    kenar2 = abs(int(input("2. kenar: ")))
    kenar3 = abs(int(input("3. kenar: ")))
    kenar4 = abs(int(input("4. kenar: ")))
    if (kenar1 == kenar2 and kenar1 == kenar3 and kenar1 == kenar4):
        print("değerlerini vermiş olduğunuz dikdörtgen karedir")
    elif ((kenar1 == kenar2 and kenar3 == kenar4 and kenar1 != kenar3) or (kenar1 == kenar3 and kenar2 == kenar4 and kenar1 != kenar2) or (kenar1 == kenar4 and kenar3 == kenar2 and kenar1 != kenar3)):
        print("değerlerini girmiş olduğunuz dörtgen bir dikdörtgendir")
    else:
        print("değerlerini girmiş olduğunuz dörtgen sıradan bir dörtgendir")
else:
    print("geçersiz geometrik şekil")