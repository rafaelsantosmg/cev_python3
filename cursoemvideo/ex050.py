"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""

from utilidadescev.dado import leiaint
from utilidadescev.string import linha

soma = 0
cont = 0
linha(25, 'amarelo')
for c in range(1, 7):
    n = leiaint(f'Digite {c}ª valor: ')
    if n % 2 == 0:
        cont += 1
        soma += n
linha(25, 'amarelo')
print(f'Você informou {c} números\n'
      f'sendo {cont} deles PARES\n'
      f'e a soma deles são {soma}')
linha(25, 'amarelo')
