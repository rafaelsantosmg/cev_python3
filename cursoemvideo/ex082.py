"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas"""

num = []
par = []
imp = []
while True:
    opc = ' '
    n = int(input('Digite um valor: '))
    num.append(n)
    while not opc in 'SN':
        opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opc in 'N':
        break
print('-*' * 20)
print(f'A lista de números gerados foram: {num}')
for pos, n in enumerate(num):
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        imp.append(n)
print(f'A lista de números pares é: {par}')
print(f'A lista de números ímpares é: {imp}')
