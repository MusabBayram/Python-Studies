def pisagor_bulma():
    pisagor_listesi = list()
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5


            if (c == int(c) and pisagor_listesi.count((j,i,c)) !=1 ):
                pisagor_listesi.append((i, j, int(c)))

    return pisagor_listesi

for i in pisagor_bulma():
    print(i)