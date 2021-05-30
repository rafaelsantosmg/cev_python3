"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor."""

from utilidadescev.dado import leia_inteiro
from utilidadescev.string import linha

linha(70)
n = leia_inteiro('Digite um valor: ')
linha(70)
if n >= 0:
    print(f'Analisando o valor {n}, seu sucessor é {n+1} e seu antecessor é {n-1}')
else:
    print(f'Analisando o valor {n}, seu sucessor é {n - 1} e seu antecessor é {n + 1}')
linha(70)
