"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles escrevendo o nome escolhido."""

from random import choice
from utilidadescev.dado import leiaNome
from utilidadescev.string import *

linha(60, 'amarelo')
a1 = leiaNome('Escreva o nome do 1º aluno: ')
a2 = leiaNome('Escreva o nome do 2º aluno: ')
a3 = leiaNome('Escreva o nome do 3º aluno: ')
a4 = leiaNome('Escreva o nome do 4º aluno: ')
linha(60, 'amarelo')
lista = [a1, a2, a3, a4]
cabeçalho(f' O aluno sorteado foi "{choice(lista)}" ', 60, 'magenta', '*', '~')
