"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de
um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""
from utilidadescev import dado

print('-' * 60)
i = dado.leiaint('Digite um número inteiro: ')
r = dado.leiafloat('Digite um número real: ')
print('-' * 60)
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
