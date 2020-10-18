"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores."""
from time import sleep
c = ('\033[m',      #  0 sem cor
     '\033[7;93m',  #  1 Amarelo
     '\033[7;94m',  #  2 Azul
     '\033[7;30m',  #  3 Branco
    );


def ajuda():
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', 1)
        msg = str(input('Função ou Biblioteca> ')).strip().lower()
        if msg in 'fim':
            break
        titulo(f'  Acessando o manual do comando \'{msg}\'', 2)
        sleep(2.5)
        print()
        print(c[3])
        help(msg)
        print(c[0])


def titulo(msg, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')


#  Programa Principal
ajuda()
