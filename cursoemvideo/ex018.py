"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo"""

from math import cos, tan, sin, radians
from utilidadescev.dado import leiafloat
from utilidadescev.string import linha

linha(65)
angulo = leiafloat('Digite um ângulo para saber seu SENO, COSSENO e TANGENTE: ')
print(f'Os valores do ângulo {angulo:.1f} são:')
print(f'SENO: {sin(radians(angulo)):.3f}')
print(f'COSSENO: {cos(radians(angulo)):.3f}')
print(f'TANGENTE: {tan(radians(angulo)):.3f}')
linha(65)
