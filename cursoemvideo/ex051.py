"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
10 primeiros termos dessa progressão."""

from utilidadescev.dado import leiaint
from utilidadescev.string import cabeçalho, linha

cabeçalho(' TERMOS DE UMA PA ', 45, 'magenta', '=', '-')
termo = leiaint('Primeiro termo: ')
razao = leiaint('Razão: ')
for c in range(1, 11):
    print(termo, end=' → ')
    termo += razao
print('Acabou!')
