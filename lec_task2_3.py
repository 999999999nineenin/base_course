a=int(input())
b=int(input())
if b==0:
    print("на ноль не дели инвалид")
else:
    if a%b==0:
        print("число a делится на число b")
    else:
        print("число a не делится на число b")
    if a%b!=0:
        print(a%b)
    print (a/b)