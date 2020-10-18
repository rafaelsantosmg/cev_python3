"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado"""

from utilidadescev.string import *
from utilidadescev.dado import leiaint

cabeçalho(' LOCADORA DE VEÍCULOS ', 60, 'azul')
dias = leiaint('Por quantos dias o carro ficou alugado? ')
km = leiaint('Quantos Km foram percorridos? ')
total = (dias * 60) + (km * 0.15)
linha(60, 'verde')
print(f'O carro ficou alugado por {dias} dia(s) e percorreu {km:.0f}Km.')
print(f'O valor total da(s) diária(s) foi R${dias * 60:.2f}')
print(f'O valor total dos Km é R${km * 0.15:.2f}')
print(f'Valor total do aluguel a ser pago R${total:.2f}')
linha(60, 'verde')
