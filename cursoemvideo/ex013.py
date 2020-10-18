"""Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento."""

from utilidadescev.dado import leiadinheiro
from utilidadescev.moeda import aumentar, moeda
from utilidadescev.string import linha

linha(65)
salario = leiadinheiro('Informe o salário atual: do funcionário: R$')
print(f'Salario de {moeda(salario)} passa a ser {aumentar(salario, 15, True)} com 15% de aumento!')
linha(65)
