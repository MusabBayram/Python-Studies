from datetime import *

while True:
    try:

        gün = int(input("Lütfen doğum gününüzü sayı olarak giriniz"))
        ay = int(input("Lütfen doğduğunuz ayı sayı olarak giriniz"))
        yıl = int(input("Lütfen doğduğunuz yılı sayı olarak giriniz"))
        şimdiki = datetime.now()
        sonuc_gün = şimdiki.day - gün
        sonuc_ay = şimdiki.month - ay
        sonuc_yıl = şimdiki.year - yıl
        if (sonuc_ay < 0):
            sonuc_yıl = sonuc_yıl - 1
            sonuc_ay = abs(sonuc_ay)
        gerekli_ay = ay-şimdiki.month
        gerekli_gün = gün-şimdiki.day
        yeni_yaş = sonuc_yıl +1
        if(gerekli_gün<0):
            gerekli_ay +=1
            gerekli_gün = abs(gerekli_gün)
        if(gerekli_ay<0):
            gerekli_ay = 12 + gerekli_ay -1
        print("{} gün {} ay ve {} yıldır yaşamaktasınız...".format(sonuc_gün, sonuc_ay, sonuc_yıl))
        print("{} yaşındayım demeniz için {} gün {} ay kalmıştır".format(yeni_yaş,gerekli_gün,gerekli_ay))
        x = input("çikmak için 'q' ya basınız, devam etmek için herhangi bir tuşa basın")
        if (x == "q"):
            break
    except:
        print("Lütfen uyarıları göze alarak bilgilerinizi verin...")
        a = input("çıkmak için q ya basınız")
        if ( a == "q"):
            break

