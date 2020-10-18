"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente."""

from utilidadescev.dado import leiaNome
from utilidadescev.string import linha

linha(60, 'amarelo')
n = leiaNome('Digite seu nome completo: ')
nome = n.split()
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[-1]}')
linha(60, 'amarelo')
