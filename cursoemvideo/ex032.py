"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

from datetime import date
from utilidadescev.dado import leiaint
from utilidadescev.string import *

linha(70, 'cinza')
ano = leiaint('Qual ano você quer analizar, coloque 0 para analisar o ano atual! ')
linha(70, 'cinza')
linha(40, 'amarelo')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')
linha(40, 'amarelo')
