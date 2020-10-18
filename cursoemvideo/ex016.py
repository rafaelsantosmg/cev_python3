"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira."""

from utilidadescev.dado import leiafloat
from utilidadescev.string import linha

linha(85)
n = leiafloat('Digite um valor real, ex n.xx..., para retornar seu valor inteiro: ')
print(f'O valor real digitado foi {n} e sua porção inteira é {int(n)} e seu valor arredondado é {round(n)}')
linha(85)
