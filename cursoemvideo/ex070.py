"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se usuário vai continuar. No final, mostra:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1.000,00.
C) Qual é o nome do produto mais barato."""

print('=*' * 25)
print('{:-^50}'.format('MERCADINHO HELCK'))
print('=*' * 25)
total = mbarato = maismil = count = 0
nbarato = ''
while True:
    print('-' * 50)
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Valor do produro R$'))
    total += preco
    count += 1
    if preco >= 1000:
        maismil += 1
    if count == 1 or preco < mbarato:
        mbarato = preco
        nbarato = nome
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('{:-^50}'.format('VENDA FECHADA'))
print(f'O total de compras foi R${total:.2f}')
print(f'{maismil} custaram mais de R$1.000,00')
print(f'O produto mais barato foi {nbarato.title()}, custou R${mbarato:.2f}')
print('{:*^50}'.format('PROGRAMA ENCERRADO'))
