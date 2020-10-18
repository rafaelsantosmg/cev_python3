"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer continuar ou não. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""

mais18 = homens = menos20 = 0
while True:
    titulo = 'CADASTRAR PESSOA'
    print('-=' * 25)
    print(f'{titulo:-^50}')
    print('-=' * 25)
    idade = ''
    while True:
        idade = input('IDADE: ')
        if not idade.isdigit():
            print("Digite apenas números!")
        else:
            break
    idade = int(idade)
    sexo = ' '
    escolha = ' '
    while sexo not in 'FM':
        sexo = str(input('SEXO [F/M]: ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1
    if sexo == 'M':
        homens += 1
    while escolha not in 'NS':
        print('-=' * 25)
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=' * 25)
print(f'{mais18} pessoa(s) cadastrada tem mais de 18 ano(s).')
print(f'{homens} pessoa(s) cadastrada são homens.')
print(f'{menos20} mulher(es) tem menos de 20 ano(s).')
print('-=' * 25)
print('PROGRAMA ENCERRADO')
