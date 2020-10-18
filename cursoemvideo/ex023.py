"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

from utilidadescev.dado import leiaint
from utilidadescev.string import linha

linha(50)
while True:
    num = leiaint('Digite um número: ')
    if num > 9999:
        print('\033[1;31mNúmero inválido! Digite um número entre 0, 9999\033[m')
        continue
    else:
        linha(50)
        break
n = str(num)
linha(40, 'azul', '=')
print(f'Analisando seu número {num}...')
linha(40, 'azul', '=')
c = 0
linha(40, 'verde')
for v in n:
    print(f'Seu número contém {v} ', end='')
    if c == 0:
        print('unidades')
    if c == 1:
        print('dezenas')
    if c == 2:
        print('centenas')
    if c == 3:
        print('milhar')
    c += 1
linha(40, 'verde')
