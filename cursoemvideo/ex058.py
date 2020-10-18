"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep
print('=+='*23)
print('-'*10, 'Vou pensar num número de 0 a 10 tente adivinhar!', '-'*10)
print('=+='*23)
palpite = 0
computador = randint(0, 10)
acertou = False
while not acertou:
    print()
    jogador = int(input('Digite seu palpite! '))
    palpite += 1
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS...', end='')
        else:
            print('MENOS...', end='')
        print('\033[31mTente novamente!\033[m')
print(f'\033[32mPARABÉNS!\033[m você adivinhou o número {computador} depois de {palpite} tentativas.')
