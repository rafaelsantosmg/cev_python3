"""Refaça o DESAFIO #35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO quando todos os seguimentos são iguais.
ISÓSCELES quando dois seguimentos são iguais.
ESCALENO quando todos os seguimentos são diferentes."""

from utilidadescev.dado import leiafloat
from utilidadescev.string import linha

#  Mostrando o tipo de TRIANGULO:
linha(25, 'cinza')
seg1 = leiafloat('Primeiro seguimento: ')
seg2 = leiafloat('Segundo seguimento: ')
seg3 = leiafloat('Terceiro seguimento: ')
linha(25, 'cinza')
linha(55, 'verde')
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1:
    print('Os seguimentos acima podem formar um triângulo ', end='')
    if seg1 == seg2 == seg3:
        print('EQUITÁTERO!')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima não podem formar um TRIÂNGULO!')
linha(55, 'verde')
