"""Faça um programa que leia nome e peso de várias pessoas, quardando tudo em ua lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = list()
dados = list()
pesadas = list()
leves = list()
maiorp = menorp = 0
while True:
    dados.append(str(input('Digite o nome: ')).strip())
    dados.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maiorp = menorp = dados[1]
    else:
        if dados[1] >= maiorp:
            maiorp = dados[1]
        if dados[1] <= menorp:
            menorp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opc = ' '
    while opc not in 'SsNn':
        opc = str(input('Cadastrar mais pessoas? [S/N]: ')).strip()[0]
    if opc in 'Nn':
        break
print('-' * 50)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas tem {maiorp}Kg e foram:')
for p in pessoas:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end=' ')
print('\n', '-' * 50)
print(f'As pessoas mais leves tem {menorp}Kg e foram:')
for p in pessoas:
    if p[1] == menorp:
        print(f'[{p[0]}]', end=' ')
