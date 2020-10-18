"""Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele ganhou no final do jogo."""

from random import randint
titulo = 'JOGO DO PAR OU IMPAR'
print('-=' * 40)
print(f'{titulo:-^80}')
print('-=' * 40)
v = 0
while True:
    print('*' * 80)
    n = int(input('Escolha um número de [1 a 10]: '))
    comp = randint(0, 10)
    total = n + comp
    parimpar = ' '
    while parimpar not in 'PI':
        parimpar = str(input('Você quer PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0]
    print('-' * 80)
    print(f'Você jogou {n} e computador {comp} = {total} ', end='')
    print('DEU PAR' if total % 2 ==0 else 'DEU ÍMPAR')
    if parimpar == 'P':
        if total % 2 == 0:
            print('Vocẽ VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif parimpar == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente! ')
print('*' * 80)
print(f'GAME OVER!, Você venceu {v} vezes!')
