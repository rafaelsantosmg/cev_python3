"""Crie um programa que faça o computador jogar Jokenpô com você."""

from time import sleep
from random import randint
from utilidadescev.dado import leiaint, menu
from utilidadescev.string import cabeçalho, linha, cores

while True:
    opcao = menu(['PEDRA', 'PAPEL', 'TESOURA', 'SAIR'], 'Vamos jogar JOKENPÔ?')
    lista = ('PEDRA', 'PAPEL', 'TESOURA')
    if opcao == 4:
        break
    linha(50)
    print(f'{cores("magenta")}JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print(f'PÔ!!!{cores("limpa")}')
    sleep(0.5)
    linha(20, 'magenta', '~')
    comp = randint(1, 3)
    if opcao == 1: #PEDRA
        if comp == 1:
            print('EMPATARAM!')
        elif comp == 2:
            print('COMPUTADOR VENCEU!')
        else:
            print('VOCÊ VENCEU!')
    elif opcao == 2: #PAPEL
        if comp == 1:
            print('VOCÊ VENCEU!')
        elif comp == 2:
            print('EMPATARAM!')
        else:
            print('COMPUTADOR VENCEU!')
    elif opcao == 3: #TESOURA
        if comp == 1:
            print('COMPUTADOR VENCEU!')
        elif comp == 2:
            print('VOCÊ VENCEU!')
        else:
            print('EMPATARAM!')
    linha(25, 'magenta', '~')
    print(f'Computador jogou {lista[comp-1]}')
    print(f'Você jogou {lista[opcao-1]}')
    linha(25, 'magenta', '~')
linha()
print('PROGRAMA ENCERRADO!')
