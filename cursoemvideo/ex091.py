"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
from operator import itemgetter
from typing import List, Any

jogo = dict()
jogo['jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)
print('*' * 30)
print('{:^30}'.format('Valores sorteados'))
print('*' * 30)
sleep(1)
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('*' * 30)
print('{:^30}'.format('RANKING DOS JOGADORES'))
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}')
    sleep(1)
