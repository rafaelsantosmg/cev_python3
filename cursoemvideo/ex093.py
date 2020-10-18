jogador = dict()
gols = list()
jogador['jogador'] = str(input('Nome: ')).strip().title()
partida = int(input(f'Quantas partidas {jogador["jogador"]} jogou? '))
for p in range(0, partida):
    gols.append(int(input(f'Quantos gols {jogador["jogador"]} marcou na {p+1} partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
print('-=' * 60)
print(jogador)
print('-=' * 60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["jogador"]} jogou {len(jogador["gols"])} partidas.')
for i, g in enumerate(gols):
    print(f' ==> Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
