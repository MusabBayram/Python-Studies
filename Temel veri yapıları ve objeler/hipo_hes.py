print("Lütfen üçgeninizin dik olan kenarlarının uzunluğunu sırasıyla giriniz..")

a = int(input("a kenarı: "))
b = int(input("b kenarı: "))

hesapla = (a**2 + b**2)**0.5

print("hipotenüsünüz: {}".format(hesapla))