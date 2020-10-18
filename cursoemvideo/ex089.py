"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

alunos = list()
cadastro = list()
media = 0
while True:
    resp = ' '
    nome = str(input('Digite o nome do aluno: '))
    cadastro.append(nome)
    for n in range(1, 3):
        nota = float(input(f'Digite a {n} nota: '))
        cadastro.append(nota)
    media = (cadastro[1] + cadastro[2]) / 2
    cadastro.append(media)
    alunos.append(cadastro[:])
    cadastro.clear()
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for p, i in enumerate(alunos):
    print(f'{p:<4} {i[0]:<10} {i[2]:>8.1F}')
print('-' * 30)
while not resp == 999:
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print(f'Notas de {alunos[resp][0]} são [{alunos[resp][1]}, {alunos[resp][2]}]')
