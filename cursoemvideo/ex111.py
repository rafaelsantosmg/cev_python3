"""Crie um pacote chamado utilidadescev que tenha dois módulos internos chamados moeda e dado. Transfira todas as
funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""
from utilidadescev import moeda

p = float(input('Digite um preço: R$'))
moeda.resumo(p, 10, 25)
print()
print(moeda.moeda(p))
print()
print(moeda.metade(p, True))
print()
print(moeda.dobro(p, True))
print()
print(moeda.aumentar(p, 10, True))
print()
print(moeda.diminuir(p, 25, True))
