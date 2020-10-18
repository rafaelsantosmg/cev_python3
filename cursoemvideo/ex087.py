"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[], [], []]
pares = []
par = coluna = num = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Informe o valor para a matriz [{l}, {c}]: '))
        matriz[l].append(num)
        if matriz[l][c] % 2 == 0:
            par += num
            pares.append(num)
print('=*' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(0, 3):
    coluna += matriz[l][2]
print('=*' * 30)
print(f'A soma de todos os valores pares {pares} são: {par}')
print(f'A soma dos números da terceira coluna são: {coluna}')
print(f'Maior valor da segunda linha é {max(matriz[1])}')
