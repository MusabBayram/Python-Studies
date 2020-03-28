print("Lütfen sırasıyla boyunuzu ve kilonuzu giriniz..")

boy = float(input("Boy: "))
kilo = int(input("Kilo: "))

indeks = kilo / boy**2

if indeks < 18.5:
    print("indeksiniz: {} çok zayıfsınız".format(indeks))
elif indeks < 25:
    print("indeksiniz: {} ideal kilodasınız tebrikler".format(indeks))
elif indeks >= 25:
    print("indeksiniz: {} obezsiniz doktora görünmeniz gerekiyor".format(indeks))


