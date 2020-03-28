def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1*(3/10) +not2*(3/10) + not3*(4/10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"
def durum_gecti(satır):
    satır = satır[:-1]
    harf_listesi = satır.split(">")
    isim_listesi = satır.split("-")
    isim = isim_listesi[0]
    harf = harf_listesi[1]

    if(harf == " FF" or harf == " FD"):
        durum = "Kaldı"
        return ""
    else:
        durum = "Geçti"
        return isim + "------------------> " + durum + "\n"
def durum_kaldı(satır):
    satır = satır[:-1]
    harf_listesi = satır.split(">")
    isim_listesi = satır.split("-")
    isim = isim_listesi[0]
    harf = harf_listesi[1]

    if(harf == " FF" or harf == " FD"):
        durum = "Kaldı"
        return isim + "------------------> " + durum + "\n"
    else:
        durum = "Geçti"
        return ""

with open ("dosya.txt", "r", encoding= "utf-8") as file:
    eklenecekler_listesi = []
    kalanlar_listesi = []
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    print(eklenecekler_listesi)
with open ("notlar.txt", "w", encoding = "utf-8") as file2:
    for i in eklenecekler_listesi:
        file2.writelines(i)
with open ("notlar.txt", "r", encoding= "utf-8") as file3:
    gecenler_listesi = []
    for i in file3:
        gecenler_listesi.append(durum_gecti(i))
with open ("gecenler.txt", "w", encoding = "utf-8") as file4:
    for i in gecenler_listesi:
        file4.writelines(i)
with open ("notlar.txt", "r", encoding= "utf-8") as file5:
    gecenler_listesi = []
    for i in file5:
        gecenler_listesi.append(durum_kaldı(i))
with open ("kalanlar.txt", "w", encoding = "utf-8") as file6:
    for i in gecenler_listesi:
        file6.writelines(i)