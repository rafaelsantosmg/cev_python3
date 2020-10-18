"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor."""

from utilidadescev.dado import leia_inteiro
from utilidadescev.string import linha

linha(60)
n = leia_inteiro('Digite um valor: ')
linha(60)
print(f'Analisando o valor {n}, seu sucessor é {n+1} e seu antecessor é {n-1}' if n is not None else '')
linha(60)
