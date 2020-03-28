print("""
      ************************************
                    işlemler:
                    1. toplama
                    2. çıkarma
                    3. çarpma
                    4. bölme
      ************************************""")

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
işlem = input("işlem seçiniz: ")

if işlem == "1":
    print("{} ile {} sayılarının toplamı {} dır".format(a,b,a+b))
    
elif işlem == "2":
    print("{} ile {} sayılarını çıkarmanın cevabı {} dır".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} sayılarının çarpımı {} dır".format(a,b,a*b))

elif işlem == "4":
    print("{} ile {} sayılarının bölmesi {} dır".format(a,b,a/b))

else:
    print("geçersiz işlem girdiniz!")
