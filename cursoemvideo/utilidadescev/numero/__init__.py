from math import sqrt


def dobro(num):
    return num * 2


def triplo(num):
    return num * 3


def raiz_quadrada(num):
    return sqrt(num)


def media(*num):
    med = 0
    for v in num:
        med += v
    return med / len(num)
