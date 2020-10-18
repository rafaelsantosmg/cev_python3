"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
 alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
from utilidadescev.dado import leiaint
from utilidadescev.string import linha

atual = date.today().year
linha(50, 'azul')
nasc = leiaint('Em que ano você nasceu? ')
sexo = str(input('Informe o sexo: M - Masculino, F - Feminino ')).upper().strip()
linha(50, 'azul')
idade = atual - nasc
linha(50, 'verde')
if sexo == "M":
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Falta {saldo} anos para você fazer o alistamento!')
        print(f'Seu alistamento será no ano de {atual + saldo}')
    else:
        saldo = idade - 18
        print(f'Já passou {saldo} anos do tempo do alistamento!')
        print(f'Seu alistamento foi no ano {atual - saldo}')
elif sexo == "F":
    print('O alistamento militar é obrigatório apenas para Homens!')
    linha(50, 'verde')
else:
    linha(30, 'vermelho')
    print('Opção inválida')
linha()
print('Tenha um bom dia!')
