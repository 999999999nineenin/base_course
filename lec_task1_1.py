import random, os

n = 15
def randomer():
    return [random.randint(99, 100) for _ in range (n)]


array_1, array_2, array_3 = randomer(), randomer(), randomer()

print(min(array_1), min(array_2), min(array_3))

if min(array_1)<100:
    os.system('python lec_task1_1.py')

