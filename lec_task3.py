from lec_constant import speed_of_freefall as g


def func(mass, height, speed):
    e=((mass  *(speed ** 2)) / 2) + (mass * g * height)
    print(e)


func(a, b, c)