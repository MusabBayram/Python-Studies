print("""
***************************

      Kullanıcı girişi

***************************""")

a = "Musab"
b = "12345"

hata_sayısı = 0

while True:
    Kullanıcı_adı = input("Kullanıcı adı:")
    Parola = input("Parola:")
    if (a != Kullanıcı_adı and b == Parola):
            print("Hatalı kullanıcı adı!")
            hata_sayısı += 1
    elif (b != Parola and a == Kullanıcı_adı ):
            print("Hatalı parola!")
            hata_sayısı += 1
    elif (a != Kullanıcı_adı and b != Parola):
        print("Böyle bir kullanıcı yok!!")
        hata_sayısı += 1
    else:
        print(""" 
        ***********************************************************
        *********************  Hoş geldiniz  **********************
        ***********************************************************""")
        break
    if hata_sayısı == 3:
        print("Çok fazla hatalı giriş yaptınız sistemden atılıyorsunuz...")
        break
