"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior."""


def sorteia():
    from random import randint
    from time import sleep
    print(f'Sorteando 5 valores ', end='')
    for n in range(0, 5):
        numeros.append(randint(0, 10))
        print(f'{numeros[n]}', end=' ')
        sleep(0.3)
    print('PRONTO')


def somapar(num):
    soma = 0
    for v in num:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {num} = {soma}')


#  Programa Principal
numeros = list()
sorteia()
somapar(numeros)
