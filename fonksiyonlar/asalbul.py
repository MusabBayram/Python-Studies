def asal_mi(sayı):
    i = 2
    while True:
        if(sayı!=1 and sayı!=i):
            if(sayı%i==0):
                return print("bu sayı asal değildir")
            break
    return print("bu sayı asal sayıdır")
while True:
    sayı = input("lütfen asallığını merak ettiğiniz bir sayı giriniz (çıkmak için q ya basınız")
    if(sayı == "q" or " "):
        print("program sonlandırılıyor...")
        break
    asal_mi(int(sayı))

