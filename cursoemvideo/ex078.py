"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista"""

num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou os valore {num}')
print(f'O maior valor digitado foi {max(num)}, nas posições ', end='')
for pos, c in enumerate(num):
    if c == max(num):
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {min(num)}, nas posições ', end='')
for pos, c in enumerate(num):
    if c == min(num):
        print(f'{pos}...', end=' ')
