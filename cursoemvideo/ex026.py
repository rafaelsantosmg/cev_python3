"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez."""

from utilidadescev.dado import leiaNome
from utilidadescev.string import linha

linha(60)
frase = leiaNome('Digite uma frase: ').upper()
print('A letra "A" aparece {}.'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))
linha(60)
