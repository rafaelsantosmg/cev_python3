"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores."""

from datetime import date
atual = date.today().year
count = 0
count2 = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        count += 1
    else:
        count2 += 1
print(f'Ao todo são {count} pessoas MAIORES DE IDADE!')
print(f'E {count2} pessoas MENORES DE IDADE!')
