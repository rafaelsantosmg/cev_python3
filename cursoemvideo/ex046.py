"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
 com uma pausa de 1 segundo entre eles."""

from time import sleep
import emoji
from utilidadescev.string import cabeçalho, linha

cabeçalho(' Fogos de Artifícios ')
print('Contagem regressiva!')
linha(50, 'verde')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks:'*10))
linha(50, 'verde')
