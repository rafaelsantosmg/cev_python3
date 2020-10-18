"""Desenvolva um programa que as duas notas de um aluno. Calcule e mostre a sua média."""

from utilidadescev.dado import leiafloat
from utilidadescev.numero import media

n1 = leiafloat('Digite 1ª nota: ')
n2 = leiafloat('Digite 2ª nota: ')
print(f'A média entre {n1} e {n2} é igual {media(n1, n2)}')
