"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores."""

n = c = tot = media = maior = menor = 0
sn = 'Ss'
while sn in 'Ss':
    n = int(input('Digite um valor: '))
    tot += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    sn = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
media = tot / c
print(f'Você digitou {c} números! ')
print(f'A média foi de {media:.1f}')
print(f'O menor número foi {menor}')
print(f'O maior número foi {maior}')
