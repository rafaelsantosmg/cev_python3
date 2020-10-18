"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;31m', end=' ')
        tot += 1
    else:
        print('\033[1;33m', end=' ')
    print(f'{c}\033[m', end=' ')
if tot == 2:
    print('\nÉ PRIMO')
    