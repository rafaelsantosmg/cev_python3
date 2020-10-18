"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possivel sobre ele."""

valor = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(valor))
print('Só tem espacoes? ', valor.isspace())
print('É um número', valor.isnumeric())
print('É alfabético? ', valor.isalpha())
print('É alfanumérico? ', valor.isalnum())
print('Está em maiúsculas? ', valor.isupper())
print('Está em minúscula? ', valor.islower())
print('Está capitalizado? ', valor.istitle())
