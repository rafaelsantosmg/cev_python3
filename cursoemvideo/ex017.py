"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o
comprimento da hipotenusa."""

from math import hypot
from utilidadescev.dado import leiafloat
from utilidadescev.string import linha

linha(70)
cops = leiafloat('Cateto Oposto: ')
cadj = leiafloat('Cateto Adjacente: ')
print(f'A hipotenusa do cateto oposto {cops} + cateto adjacente {cadj} é {hypot(cops, cadj):.2f}')
linha(70)
