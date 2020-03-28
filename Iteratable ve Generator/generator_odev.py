def asal():

    while True:
        for i in range(2,1000):
            sayac = 0
            for j in range(2,i):
                if (i % j == 0):
                    sayac += 1
            if (sayac == 0):
                yield i
        break

for sayı in asal():
    print(sayı)