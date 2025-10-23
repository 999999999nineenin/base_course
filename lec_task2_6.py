a=1
b=1
while b!=10:
    for i in range(9):
        print(b*a, end=' ')
        a+=1
    a=1
    print(end='\n')
    b+=1