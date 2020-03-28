print(""""***********

Select Operation:

1: Addition

2: Substraction

3: Multiplication

4: Division

5: Exit

**************""")
while True:
    a = int(input("Press enter an Integer:"))
    b = int(input("Press enter a second Integer:"))

    işlem = input("Press enter a choice:")


    if işlem == "1":
        print("{} and {} additions is : {} .".format(a,b,a+b))
    elif işlem =="2":
        print("{} and {} substraction is : {}".format(a,b,a-b))
    elif işlem =="3":
        print("{} and {} multiplation is : {}".format(a,b,a*b))
    elif işlem =="4":
        print("{} and {} division is : {}".format(a,b,a/b))
    elif işlem=="5":
        print("Programdan cıkıyorsunuz..")
        break
