"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""

from time import sleep
'''n = int(input('Digite um número para calcular o fatorial: '))
n1 = n
print(f'Calculando {n}...', end=' = ')
sleep(2)
for c in range(n-1, 0, -1):
    print(f'{n1} x {c}', end='')
    n1 = ''
    n = n * c
print(f' = {n}')'''

n = int(input('Digite um número para calcular o fatorial: '))
print(f'Calculando {n}...', end=' = ')
sleep(2)
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
