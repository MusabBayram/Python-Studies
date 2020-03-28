sayı = int(input("binary sisteme cevirelecek olan sayıyı giriniz:"))
liste = []
binary = ""
while True:
    liste.append(sayı % 2)
    sayı = sayı //2
    if(sayı == 0):
        i = len(liste)
        while i>0:
            binary += str(liste[i-1])
            i -=1
        print(binary)
        break