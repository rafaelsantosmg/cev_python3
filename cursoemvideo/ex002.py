from utilidadescev.string import linha
from utilidadescev.dado import leia_nome

linha()
nome = leia_nome('Qual seu nome? ')
print(f'Prazer em conhece-lo {nome}' if nome is not None else '')
linha()
