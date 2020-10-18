"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""


def area(larg, comp):
    a = larg * comp
    print(f'O terreno de dimensões: largura {larg:.2f}m x comprimento {comp:.2f}m, tem uma área de {a:.2f}m².')


#  Programa Principal
print('-=' * 10)
print(f' CÁLCULO DE TERRENO')
print('-=' * 10)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
