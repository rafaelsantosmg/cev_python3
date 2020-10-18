"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

from utilidadescev.dado import leiadinheiro
from utilidadescev.moeda import moeda, aumentar
from utilidadescev.string import linha

# Vamos pedir o valor do salário ao usuário.
linha(60, 'amarelo')
salario = leiadinheiro('Qual é o salário do funcionário? R$')
linha(60, 'amarelo')

# Vamos calcular o aumento do salário 10% se receber acima de R$1250,00
if salario > 1250:
    linha(40, 'azul')
    print('Seu aumento foi de 10%')
    print(f'Seu salário atual é {aumentar(salario, 10, True)}')
    linha(40, 'azul')
# Vamos calcular o aumento do salário 15% se receber abaixo ou igual a 1250,00
else:
    linha(40, 'verde')
    print('Seu aumento foi de 15%')
    print(f'Seu salário atual é {aumentar(salario, 15, True)}')
    linha(40, 'verde')
