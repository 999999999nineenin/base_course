print('заполните массив:')
a=int(input())
b=[]
b.append(a)
c=0
while a!=0 and c!=9:
    a=int(input())
    b.append(a)
    c+=1
print(b)
print('введите число:')
d=int(input())
print('введите позицию:')
e=int(input())
slice=b[:e]
slice.append(d)
slice_1=b[e:]
print(slice+slice_1)