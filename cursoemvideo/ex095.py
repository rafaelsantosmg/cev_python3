"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador."""
jogador = dict()
time = list()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['jogador'] = str(input('Nome do jogador: ')).strip().title()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["jogador"]} jogou? '))
    for p in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols {jogador["jogador"]} marcou na {p+1} partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod. ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k+1:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
print('-=' * 30)
while True:
    busca = int(input('Informe o número do jogador para abrir o detalhamento! (999 para parar): '))
    if busca == '999':
        break
    if busca >= len(time) or busca == 0:
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        if busca != 0:
            busca -= 1
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["jogador"]}')
        for k, g in enumerate(time[busca]["gols"]):
            print(f'  Na partida {k+1} fez {g} gol(s)')
    print('-=' * 30)
print('<< VOLTE SEMPRE >>')
