"""Crie um programa que vai gerar cinco números aleatório e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla"""

from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO menor valor sorteado foi: {min(tupla)}')
print(f'O maior valor sorteado foi: {max(tupla)}')
