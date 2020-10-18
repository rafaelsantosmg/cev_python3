"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar"""

from utilidadescev.string import linha
from utilidadescev.moeda import compra_dolar
from utilidadescev.dado import leiadinheiro

linha(40, 'verde')
valor = leiadinheiro('Quanto você tem na varteira? R$')
print(f'Você pode comprar {compra_dolar(valor)}')
linha(40, 'verde')
