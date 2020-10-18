"""Escreva um programa que converta uma temperatura digitada em ªC e converta para ªF"""

from utilidadescev.dado import leiafloat
from utilidadescev.string import linha

linha(60)
cel = leiafloat('Informe a temperatura em ºC para conversão em ºF: ')
fah = (cel * 9 / 5) + 32
print(f'A temperatura informada de {cel:.1f}ºC é {fah:.1f}ºF!')
linha(60)
