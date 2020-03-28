sayi_listesi = [1, 12, 2, 5, 6, 1, 8, 55, 8, 8, 2, 17]
say = 0
for i in range(1,len(sayi_listesi)):
    for j in range((len(sayi_listesi)-i)):
        if sayi_listesi[j] > sayi_listesi[j + 1]:
            temp = sayi_listesi[j]
            sayi_listesi[j] = sayi_listesi[j + 1]
            sayi_listesi[j + 1] = temp
    say +=1
print(sayi_listesi,say)