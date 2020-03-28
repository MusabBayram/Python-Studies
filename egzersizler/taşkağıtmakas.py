import random
import time
print("""
    ************************************************************
    * Taş kağıt makas oyununa hoş geldiniz bu oyunda rakibiniz *
    * ben olacağım hazırsanız kurallardan bahsedeyim:          *
    * taşı seçmek için '1' kağıdı seçmek için'2' makası seçmek *
    * için lütfen '3' komutunu kullanınız.(çıkmak için 'q')    *
    ************************************************************""")
while True:
    liste = ["taş","kağıt","makas"]
    kullanıcının_seçimi = input("Hazır olduğunuzda seçiminizi yapınız")
    bilgisayarın_seçimi = random.randint(1,3)
    if(kullanıcının_seçimi == "q"):
        print("program sonlandırılıyor...")
        time.sleep(1)
        print("program sonlandırılıyor...")
        time.sleep(1)
        print("program sonlandırılıyor...")
        break
    else:
        kullanıcının_seçimi = int(kullanıcının_seçimi)
        print("seçiminiz: ", liste[kullanıcının_seçimi-1])
        if(kullanıcının_seçimi<0 or kullanıcının_seçimi>3):
            print("Lütfen verilen seçenekleri giriniz")
        elif (kullanıcının_seçimi == 1 and bilgisayarın_seçimi == 2 or kullanıcının_seçimi == 2 and bilgisayarın_seçimi == 3 or kullanıcının_seçimi == 3 and bilgisayarın_seçimi == 1):
            print("xxxx kaybettiniz xxxx\nbilgisayarın seçimi:", liste[bilgisayarın_seçimi - 1])
        elif (kullanıcının_seçimi == bilgisayarın_seçimi):
            print("----berabere---- \nikinizde {} tercihini yaptınız".format(liste[bilgisayarın_seçimi - 1]))
        else:
            print("<3<3<3 tebrikler kazandınız <3<3<3\nbilgisayarın seçimi: ",liste[bilgisayarın_seçimi-1])
        print("---------------------------------------------------")
