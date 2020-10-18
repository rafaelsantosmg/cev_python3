"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

from utilidadescev.dado import leiaint
from utilidadescev.string import linha, cabeçalho

linha(45, 'verde')
n = leiaint('Digite um número para mostrar sua tabuada: ')
linha(45, 'verde')
cabeçalho(f' TABUADA DO {n} ', 20, 'azul', '=', '-')
linha(14, 'cinza')
for c in range(1, 11):
    print(f' {n} X {c:2} = {c*n}')
linha(14, 'cinza')
