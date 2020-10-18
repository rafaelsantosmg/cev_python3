"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1."""

print('=*' * 25)
print('{:-^50}'.format('CAIXA ELETRÔNICO'))
print('{:-^50}'.format('Cédulas disponiveis R$50, R$20, R$10, R$1'))
print('=*' * 25)
vsaque = int(input('Quanto quer sacar? '))
ced = 50
totced = 0
print('-' * 50)
print(f'Você sacou R${vsaque:.2f} verifique as cédulas fornecida:')
while True:
    if vsaque >= ced:
        vsaque -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if vsaque == 0:
            break
print('-' * 50)
print('{:*^50}'.format('TRANSAÇÃO ENCERRADA, VOLTE SEMPRE'))
