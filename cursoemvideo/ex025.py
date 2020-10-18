"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""

from utilidadescev.dado import leiaNome
from utilidadescev.string import linha

linha(60)
nome = leiaNome('Escreva seu nome completo: ')
print(f'Seu nome: {nome}.')
print(f'Seu nome tem "Silva"? {"silva" in nome.lower()}')
linha(60)
