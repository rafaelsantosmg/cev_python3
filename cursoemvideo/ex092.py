"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import datetime
cad = dict()
cad['nome'] = str(input('Nome: ')).strip().title()
cad['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
cad['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cad['ctps'] != 0:
    cad['contratação'] = int(input('Ano de Contratação: '))
    cad['salário'] = float(input('Salário: R$'))
    cad['aposentadoria'] = cad['idade'] + ((cad['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in cad.items():
    print(f' - {k} tem o valor {v}')
print('-=' * 30)
