"""Crie um programa que vai ler vário números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se valor 5 foi digitado e esta ou não na lista."""

num = []
cont = 0
while True:
    opc = ' '
    n = int(input('Digite um valor: '))
    num.append(n)
    cont += 1
    while not opc in 'SN':
        opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opc in 'N':
        break
print('-' * 40)
print(f'Você digitou {cont} números!')
print(f'Os valores em ordem decrescente são {sorted(num, reverse=True)}')
print(f'O valor 5 está na lista' if 5 in num else 'O valor 5 não está na lista')
