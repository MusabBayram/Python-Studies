
dize = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

say = dict()
for i in dize:
    if (i in say):
        say[i] +=1
    else:
        say[i] = 1
print(say)