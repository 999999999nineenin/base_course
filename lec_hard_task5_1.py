a=int(input())
b=1 #число
for i in range(a):
    b+=1
    c=0 #сумма делителей
    d=2 #делитель
    while b!=d:
        if b%d==0:
            c+=d
            d+=1
        else:
            d+=1
    if b==c/2:
        print(b)
print(b)