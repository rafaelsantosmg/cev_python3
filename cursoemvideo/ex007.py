"""Desenvolva um programa que as duas notas de um aluno. Calcule e mostre a sua média."""

from utilidadescev.dado import leia_real
from utilidadescev.numero import media

n1 = leia_real('Digite 1ª nota: ')
n2 = leia_real('Digite 2ª nota: ')
print(f'A média entre {n1} e {n2} é igual {media(n1, n2):.2f}')
