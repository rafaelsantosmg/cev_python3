"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:"""

frase = str(input('Digite uma frase: ')).strip().upper().split()
juntas = ''.join(frase)
inverso = juntas[::-1]
if inverso == juntas:
    print(f'{juntas} é um PALÍNDROMO "{inverso}"')
else:
    print(f'{juntas} não é um PALÍNDROMO "{inverso}"')
