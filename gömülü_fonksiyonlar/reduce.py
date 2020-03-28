from functools import reduce
def cift_mi(demet):
    if(demet %2 == 0):
        return True
    else:
        return False
def toplam(x,y):
    return x+y

liste = [1,2,3,4,5,6,7,8,9,10]
liste1 = list(filter(cift_mi,liste))

liste2 = reduce(toplam,liste1)
print(liste2)