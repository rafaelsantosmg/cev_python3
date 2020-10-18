"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:"""
from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        for c in range(i, f+1, p):
            print(f'{c}', end=' ')
            sleep(0.4)
    if i > f or f < 0:
        for c in range(i, f-1, -p):
            print(f'{c}', end=' ')
            sleep(0.4)
    print('FIM')
    print('-=' * 20)


#  Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))
