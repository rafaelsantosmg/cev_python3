"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número ja exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente."""

valores = []
while True:
    escolha = ' '
    n = int(input(f'Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print(f'Valor duplicado, não vou adicionar!')
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha in 'N':
        break
print(f'O valores cadastrados foram {sorted(valores)}')
