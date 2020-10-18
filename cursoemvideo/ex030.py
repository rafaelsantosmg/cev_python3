"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

from utilidadescev.dado import leiaint
from utilidadescev.dado import *

cabeçalho(' HELCK SOFTWARES ', 60, 'magenta', '=', '*')
while True:
    linha(60, 'amarelo')
    n = leiaint('Digite um número inteiro: ')  # Valor recebido pelo usuário.
    linha(60, 'amarelo')
    if n % 2 == 0:
        print(f'O numero {n:.0f} é PAR!')
    else:
        print(f'O número {n:.0f} é IMPAR!')
    linha(60, 'amarelo')
    while True:
        resp = str(input('Finalizar o programa? SIM ou NÃO ')).strip().upper()[0]
        if resp not in 'SN':
            print('\033[1;31mOpção inválida!\033[m Digite apenas S(SIM) ou N(NÃO)')
        else:
            break
    if resp in 'S':
        break
linha(60, 'amarelo')
cabeçalho(' Obrigado por utilizar nossos SOFTWARES! ', 60, 'magenta', '=', '*')
