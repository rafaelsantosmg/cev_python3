"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

from utilidadescev.dado import leiadinheiro, menu
from utilidadescev.string import cabeçalho, linha

cabeçalho(' HELCK SOFTWARES ', 60, 'magenta', '=', '*')

while True:
    preco = leiadinheiro('Preço das compras: ')
    opcao = menu(['à vista dinheiro/cheque', 'à vista cartão', '2x no cartão', '3x no cartão ou mais', 'sair do programa'],
                 'FORMAS DE PAGAMENTO')
    linha()
    if opcao == 1:
        total = preco - (preco * 10 / 100)
    elif opcao == 2:
        total = preco - (preco * 5 / 100)
    elif opcao == 3:
        total = preco
        totparc = preco / 2
        print(f'Sua compra será parcelado em 2x de {totparc}')
    elif opcao == 4:
        total = preco + (preco * 20 / 100)
        parcela = int(input('Quantas parcelas? '))
        totparc = total / parcela
        print(f'Sua compra será parcelado em {parcela}x de R${totparc:.2f} COM JUROS')
    elif opcao == 5:
        break
    else:
        total = preco
        print('\033[1;31mOpção Inválida!\033[0m')
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f}')
    linha()
linha()
print('PROGRAMA ENCERRADO!')
