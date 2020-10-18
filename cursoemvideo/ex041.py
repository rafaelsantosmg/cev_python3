"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima: MASTER"""

from datetime import date
from utilidadescev.dado import leiaint
from utilidadescev.string import linha

#  Leitura de idade para classificação de Natação:
linha(50, 'cinza')
nasc = leiaint('Qual o ano de nascimento do atleta? ')
linha(50, 'cinza')
atual = date.today().year
idade = atual - nasc
linha(50, 'verde')
if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Classificação MIRIM!')
elif idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Classificação INFANTIL!')
elif idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('Classificação JUNIOR!')
elif idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação SÊNIOR!')
elif idade > 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação MASTER!')
linha(50, 'verde')
