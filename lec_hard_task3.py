a=int(input())
b=len(str(a))
c=10
while b!=0:
    print(a%c, end='')
    b=b-1
    a=a//10