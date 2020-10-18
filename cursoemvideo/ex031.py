"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

from utilidadescev.dado import leiafloat
from utilidadescev.string import *

cabeçalho(' Olá seja BEM VINDO! ', 60, 'magenta', '=', '*')
linha(40, 'verde')
km = leiafloat('Digite a distancia da viagem em Km: ')  # Usuário deve entrar com a quantidade de Km
linha(40, 'verde')
#  Preço da passagem até 200Km é R$0,50
#  Preço da passagem acima de 200Km é R$0,45
preco = km * 0.5 if km <= 200 else km * 0.45
linha(40, 'vermelho')
print(f'Sua Passagem vai custar R${preco:.2f}')
linha(40, 'vermelho')
