"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
o empréstimo será negado."""

from utilidadescev.dado import leiadinheiro, leiaint
from utilidadescev.string import *
from utilidadescev.moeda import moeda

#  Financiamento Imobiliário sem opção de juros.
linha(60, 'magenta')
casa = leiadinheiro('Quanto custa a casa? ')
salario = leiadinheiro('Quanto você ganha? ') * 30 / 100
anos = leiaint('Em quantos anos você quer pagar? ') * 12
linha(60, 'magenta')
parcela = casa / anos
#  Condição de financiamento: O valor da parcela não pode exceder 30% do salário do comprador!
if parcela <= salario:
    linha(65, 'verde')
    print('Seu financiamento foi APROVADO!')
    print(f'Valor a ser financiado {moeda(casa)} em {anos} prestações de {moeda(parcela)}')
    linha(65, 'verde')
#  Se valor da parcela for superior a 30% do salário.
else:
    linha(65, 'vermelho')
    print('Infelizmente seu financiamento foi REPROVADO!')
    print(f'Valor da parcela {moeda(parcela)} e 30% do seu salário {moeda(salario)}')
    linha(65, 'vermelho')
linha()
print('Obrigado volte sempre!')
