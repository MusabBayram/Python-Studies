
sayı = int(input("lütfen çarpım tablosu için bi sınır belirtin: "))
print("**************************************")
for i in range(1,sayı+1):
    for j in range(1,sayı+1):
        k = i*j
        print("{} * {} = {}".format(i,j,k) )
    print("**************************************\n**************************************")