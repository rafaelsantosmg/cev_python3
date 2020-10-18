"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. """

from time import sleep
print('='*30)
num1 = int(input('Digite 1ª valor: '))
num2 = int(input('Digite 2ª valor: '))
opcao = 0
while opcao != 5:
    print('=' * 30)
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR''')
    print('=' * 30)
    print('-'*30)
    opcao = int(input('Escolha a opção desejada: '))
    print('-' * 30)
    if opcao == 1:
        total = num1 + num2
        print(f'\033[1;33mA soma de {num1}, {num2} = {total}.\033[m')
    elif opcao == 2:
        total = num1 * num2
        print(f'\033[1;33mA multiplicação de {num1}, {num2} = {total}.\033[m')
    elif opcao == 3:
        if num1 > num2:
            print(f'\033[1;33mO número {num1} é MAIOR que {num2}.\033[m')
        else:
            print(f'\033[1;33mO número {num2} é MAIOR que {num1}.\033[m')
    elif opcao == 4:
        num1 = int(input('Digite 1ª valor: '))
        num2 = int(input('Digite 2ª valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção inválida')
    sleep(1.5)
print('\033[1;31mPROGRAMA ENCERRADO!\033[m')
