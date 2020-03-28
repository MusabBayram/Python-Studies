def ucgen_mi(demet):
    if (demet[0]+demet[1]<demet[2] or demet[0]+demet[2]<demet[1] or demet[2]+demet[1]<demet[0]):
        return False
    else:
        return True

liste = [(3,4,5),(6,8,10),(3,11,7),(1,1,20)]
print(list(filter(ucgen_mi,liste)))