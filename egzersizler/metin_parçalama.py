while True:
    mtn = input("\nbiraderim sana zahbet bişekler yaz bakalım:")
    liste = mtn
    #print(" ".join(mtn))
    mtn = mtn.replace("a", "o")
    mtn = mtn.replace("e", "o")
    mtn = mtn.replace("ı", "o")
    mtn = mtn.replace("i", "o")
    mtn = mtn.replace("ö", "o")
    mtn = mtn.replace("u", "o", )
    mtn = mtn.replace("ü", "o", )
    print("\n"+mtn)
    if(mtn == "q"):
        break

