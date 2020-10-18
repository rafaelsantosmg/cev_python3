"""Crie um programa que leia dois números e mostre a soma entre eles"""

from utilidadescev.dado import leia_real
from utilidadescev.string import linha

linha()
n1 = leia_real('Digite um valor: ')
if n1 is not None:
    n2 = leia_real('Digite um valor: ')
    if n2 is not None:
        soma = n1 + n2
        linha()
        print(f'A soma dos dois valores são {soma}')
        linha()
