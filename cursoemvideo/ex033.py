"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

from utilidadescev.dado import leiaint
from utilidadescev.string import linha

linha(40, 'magenta')
n1 = leiaint('Primeiro valor: ')
n2 = leiaint('Segundo valor: ')
n3 = leiaint('Terceiro valor: ')
linha(40, 'magenta')
# Descobrindo menor valor.
linha(40, 'azul')
if n1 < n2 and n1 < n3:
    print(f'Menor número é: {n1}')
if n2 < n1 and n2 < n3:
    print(f'Menor número é: {n2}')
if n3 < n1 and n3 <n2:
    print(f'Menor número é: {n3}')
# Descobrindo maior valor.
if n1 > n2 and n1 > n3:
    print(f'Maior número é: {n1}')
if n2 > n1 and n2 > n3:
    print(f'Maior número é: {n2}')
if n3 > n1 and n3 > n2:
    print(f'Maior número é: {n3}')
linha(40, 'azul')
