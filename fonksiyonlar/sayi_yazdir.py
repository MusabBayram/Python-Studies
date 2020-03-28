def yazdır(sayı):

    sd_bas= sayı//10
    birinci = sayı %10
    str1 = ["","On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
    str2 = ["","bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    yaz = ""

    return str1[sd_bas] + " " + str2[birinci]

while True:

    sayı = input("Lütfen 2 basamaklı bir sayı giriniz. Çıkmak için q ya basınız: ")

    if(sayı == "q"):
        break
    sayı = int(sayı)

    if(not(sayı > 9 and sayı < 100)):
        print("geçersiz sayı")
        continue

    print(yazdır(sayı))

