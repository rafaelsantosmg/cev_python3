"""Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiro colocados.
B) Os últimos 4 colocados.
C) Uma lista com times em ordem alfabética.
D) Em que posição da tabela está o time da Chapecoense."""

tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', ' Atlético-Paranaense', 'São-Paulo', 'Internacional',
          'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco-da-Gama', 'Atlético-Mineiro', 'Fluminense', 'Botafogo',
          'Ceará', 'Cruzeiro', 'Csa-AL', 'Chapecoense', 'Avaí')
print(f'Os 5 primeiros colocados são {tabela[0:6]}')
print(f'Os 4 últimos colocados são {tabela[15:]}')
print(f'A lista dos times organizada em ordem alfabética: {sorted(tabela)}')
print('O time da Chapecoense está na {} posição!'.format(tabela.index('Chapecoense')+1))
