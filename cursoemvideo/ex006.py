"""Crie um algoritimo que leia um número e mostre o seu dobro triplo e raiz quadrada"""

from utilidadescev.dado import leia_inteiro
from utilidadescev.numero import *

n = leia_inteiro('Digite um número: ')
dobro(n)
triplo(n)
raiz_quadrada(n)
print(f'O dobro de {n} = {dobro(n)} o triplo = {triplo(n)} e raiz quadrada = {raiz_quadrada(n):.2f}!'
      if n is not None else '')
