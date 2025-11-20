print('заполните массив:')
a=int(input())
b=[]
b.append(a)
c=0
while a!=0 and c!=9:
    a=int(input())
    b.append(a)
    c+=1
c+=1
print(b)
print('введите число:')
d=int(input())
print('введите позицию:')
e=int(input())
if e-1>c:
    print('размерность массива слишком мала')
else:
    slice=b[:e-1]
    slice.append(d)
    slice_1=b[e-1:]
    print(slice+slice_1)