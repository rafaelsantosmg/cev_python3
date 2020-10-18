"""Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuario. O programa será interrompido quando o
número solicitado for negativo."""

titulo = 'PROGRAMA DE TABUADA'
print('-=' * 22)
print(f'{titulo:-^44}')
print('-=' * 22)
while True:
    n = int(input('Informe o número para saber sua TABUADA: '))
    print('-=' * 22)
    if n < 0:
        break
    print(f'A tabuada de {n} é:')
    for count in range(1, 11):
        print(f'{n} x {count:2} = {n * count}')
    print('-=' * 22)
print('PROGRAMA TABUADA ENCERRADA!')
