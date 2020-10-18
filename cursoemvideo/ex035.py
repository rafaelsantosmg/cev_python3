"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo."""

from utilidadescev.dado import leiafloat
from utilidadescev.string import *

cabeçalho(' ANALISADOR DE TRIÂNGULO ', 45, 'magenta', '=', '~')
linha(45, 'azul')
seg1 = leiafloat('Primeiro seguimento: ')
seg2 = leiafloat('Segundo seguimento: ')
seg3 = leiafloat('Terceiro seguimento: ')
linha(45, 'azul')
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    linha(40, 'amarelo')
    print('É possivel formar o TRIÂNGULO!')
    linha(40, 'amarelo')
else:
    linha(40, 'vermelho')
    print('Não é possivel formar o TRIÂNGULO!')
    linha(40, 'vermelho')
