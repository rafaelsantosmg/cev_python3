"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m"""

from utilidadescev.dado import leiafloat
from utilidadescev.string import linha, cabeçalho

linha(60, 'azul')
larg = leiafloat('Informe a largura da parede: ')
alt = leiafloat('Informe a altura da parede: ')
linha(60, 'azul')
area = larg * alt
tinta = area / 2
cabeçalho(f'A parede tem {area:.2f}m² e será necessário {tinta:.3f}lts de tinta!', 60, 'verde')
