
sayı = int(input("mukemmelliği hesaplanacak sayı: "))

toplam = 0
for i in range(1,sayı):
    if (sayı%i==0):
        toplam += i
if (toplam == sayı):
    print("bu sayı Mükemmel bir sayıdır",sayı)
else:
    print("mukemmel değil bu sayı")