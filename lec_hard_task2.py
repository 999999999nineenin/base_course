a=int(input())
b=int(input())
c=int(input())
if a < b+c and b < a+c and c < a+b:
    if a==b==c:
        print("треугольник равносторонний")
    elif a==b or a==c or b==c:
        print("треугольник равнобедренный")
    else:
        print("треугольник разносторонний")
else:
    print("треугольник не существует")