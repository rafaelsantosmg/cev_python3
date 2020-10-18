"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}ª pessoa: '))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print(f'O maior peso infomado foi Kg{pesomaior:.1f}')
print(f'O menor peso informado foi Kg{pesomenor:.1f}')
