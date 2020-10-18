"""Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros"""

from utilidadescev.dado import leiafloat

n = leiafloat('Digite a metragem: ')
km = n / 1000
hec = n / 100
dam = n / 10
dec = n * 10
cent = n * 100
milim = n * 1000
print(f'{km:.3f}km')
print(f'{hec:.2f}hm')
print(f'{dam:.1f}dam')
print(f'{dec:.0f}dm')
print(f'{cent:.0f}cm ')
print(f'{milim:.0f}mm!')
