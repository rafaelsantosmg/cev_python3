"""Faça um programa que leia nome e média de uma aluno, guardando também a situação em um dicionário.
No final, mostre o conteudo da estrutura na tela."""
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 < aluno['Média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÂO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v} ')
