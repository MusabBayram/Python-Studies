
fibonacci = []
sayı = int(input("fibonaccinin sınırını belirleyiniz:"))

a = 1
b = 1
fibonacci.append(a)
fibonacci.append(b)
for i in range(sayı):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)