"""Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle
from utilidadescev.dado import leiaNome
from utilidadescev.string import *

cabeçalho(' PROGRAMA SORTEIA ALUNO ', 40, 'azul', '=', '*')
linha(40, 'amarelo')
a1 = leiaNome('Escreva o nome do 1º aluno: ')
a2 = leiaNome('Escreva o nome do 2º aluno: ')
a3 = leiaNome('Escreva o nome do 3º aluno: ')
a4 = leiaNome('Escreva o nome do 4º aluno: ')
linha(40, 'amarelo')
lista = [a1, a2, a3, a4]
shuffle(lista)
linha(40, 'cinza')
print('A ordem do sorteio foi: ')
for i, v in enumerate(lista):
    print(f'{i+1}º \t{v}', end='\n')
linha(40, 'cinza')
