"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- A)O nome com todas as letras maiúsculas e minúsculas.
- B)Quantas letras ao todo (sem considerar espaços).
- C)Quantas letras tem o primeiro nome."""

from utilidadescev.dado import leiaNome
from utilidadescev.string import cabeçalho, linha

cabeçalho(' ANALISANDO NOMES ', 50, 'azul', '=', '-')
linha(50, 'amarelo')
nome = leiaNome('Digite o nome completo: ')
print('Analisando seu nome...')
print(f'Seu nome em MAIÚSCULO é: {nome.upper()}!')
print(f'Seu nome em minúsculo é: {nome.lower()}!')
print(f'O nome contém {len(nome) - nome.count(" ")} letras sem espaços!')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e contém {len(separa[0])} letras!')
linha(50, 'amarelo')
