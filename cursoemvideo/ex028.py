"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar des-
cobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep
from utilidadescev.string import *
from utilidadescev.dado import leiaint

while True:
    n1 = randint(0, 5)
    cabeçalho('Olá vou pensar num número de 0 a 5 tente adivinhar!', 55)
    while True:
        n2 = leiaint('Digite o número: ')
        if n2 > 5:
            print('\033[1;31mNúmero inválido!\033[m Digite um número de 0 a 5!')
            continue
        else:
            break
    print('PROCESSANDO...')
    sleep(2)
    linha(55, 'cinza')
    print(f'O número escolhido por mim foi {n1}!')
    linha(55, 'cinza')
    if n2 == n1:
        linha(35, 'verde')
        print('PARABÉNS! Você advinhou meu número!')
        linha(35, 'verde')
    else:
        linha(35, 'vermelho')
        print('Infelimento você ERROU!')
        linha(35, 'vermelho')
    while True:
        linha(35)
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp not in 'SN':
            print('\033[1;31mOpção inválida!\033[m Digite apenas S ou N!')
            continue
        else:
            break
    if resp in 'N':
        break
