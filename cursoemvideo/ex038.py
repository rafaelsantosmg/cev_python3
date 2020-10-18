"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:"""

from utilidadescev.dado import leiafloat
from utilidadescev.string import linha

linha(25, 'azul')
num1 = leiafloat('Primeiro número: ')
num2 = leiafloat('Segundo número: ')
linha(25, 'azul')
linha(25, 'amarelo')
if num1 > num2:
    print('Primeiro número é MAIOR')
elif num2 > num1:
    print('Segundo número é MAIOR')
else:
    print('Os número são IGUAIS')
linha(25, 'amarelo')
