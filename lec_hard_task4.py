a=int(input())
b=2
c=1
d=[]
while c>1:
    d=c
    c=c-1
while a > 1:
    if a%2==0:
        a=a/b
        if c%d!=0:
            c=c
        else:
            c+=1
        b=2+c
