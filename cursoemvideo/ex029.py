"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

from time import sleep
from utilidadescev.dado import leiaint
from utilidadescev.string import *

cabeçalho(' RADAR ELETRÔNICO ', 50, 'cinza', '=', '*')
linha(50, 'verde')
velocidade = leiaint('Digite a velocidade do veículo: ')
sleep(1.5)
linha(50, 'verde')
if velocidade > 80:
    linha(30, 'vermelho')
    print('ATENÇÃO VOCÊ FOI MULTADO!')
    linha(30, 'vermelho')
    linha(60)
    print('Você excedeu o limite de velocidade de 80Km/h!')
    print('Tera que pagar R$7,00 por Km/h ultrapassados acima do limite.')
    print(f'Sua multa ficou no valor de R${(velocidade-80)*7:.2f}')
    linha(60)
else:
    linha(42, 'amarelo')
    print('Você está dentro do limite de velocidade!')
    linha(42, 'amarelo')
linha(40)
print('Tenha um bom dia, dirija com segurança!')
