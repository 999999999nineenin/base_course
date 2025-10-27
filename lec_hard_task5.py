a=int(input())
b=1
c=2
d=0
for i in range (a):
    b+=1
    while b<=c:
        if b%c==0:
            d+=c
            break
        else:
            c+=1
    if b==d/2:
        print(b)
print(b)
print(c)
print(d)