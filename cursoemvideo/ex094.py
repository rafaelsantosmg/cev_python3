"""Crie um programa que leia nome, sexo e idade de várias pessoas, quardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A)Quantas pessoas cadastradas.
B)A média de idade.
C)Uma lista com mulheres.
D)Uma lista com idade acima da média."""
cad = dict()
pessoa = list()
while True:
    print('-=' * 30)
    cad['nome'] = str(input('Nome: ')).title()
    resp = sexo = ' '
    soma = cont = 0
    while sexo not in 'FM':
        sexo = str(input(f'Sexo de {cad["nome"]} [F/M]: ')).strip().upper()[0]
        if sexo not in 'FM':
            print('Erro! Por favor, digite apenas F ou M.')
    cad['sexo'] = sexo
    cad['idade'] = int((input(f'Idade de {cad["nome"]}: ')))
    pessoa.append(cad.copy())
    cad.clear()
    while resp not in 'SN':
        resp = str(input('Novo cadastro? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('Erro! Por favor, digite apenas S ou N.')
    if resp in 'N':
        break
for c in range(0, len(pessoa)):
    soma += pessoa[c]['idade']
media = soma / len(pessoa)
print(pessoa)
print('-=' * 30)
print(f'A) Foram cadastradas {len(pessoa)} pessoas.')
print(f'B) A média de idade das pessas cadastrada foi {media:5.2f}')
print('C) As mulheres cadastradas foram: ', end='')
for n in pessoa:
    if n['sexo'] == 'F':
        print(f'{n["nome"]}', end=' ')
print()
print(f'D) As pessoas com idade acima da média são: ')
for p in pessoa:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('PROGRAMA ENCERRADO')
