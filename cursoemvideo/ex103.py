"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
tenha sido informado corretamente."""


def ficha(nome='', gols=''):
    if gols.isnumeric():
        int(gols)
    else:
        gols = 0
    if nome == '':
        nome = '<Desconhecido>'
    return print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


#  Programa Principal
ficha(str(input('Nome do Jogador: ')).strip().title(),
      str(input('Quantos gols ele marcou? ')).strip())
