a=int(input())
b=2
d=[]
while a > 1:
    if a%b==0:
        a=a/b
        d.append(b)
        b=2
    else:
        b+=1
print(d)