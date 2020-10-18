def dobro(num):
    return num * 2


def triplo(num):
    return num * 3


def raiz_quadrada(num):
    return num ** (1/2)


def media(*num):
    med = 0
    for v in num:
        med += v
    return med / len(num)
