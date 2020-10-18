"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no
intervalo de 1 até 500."""

soma = count = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        count += 1
print()
print(f'A Soma dos {count} números ímpares de 1 a 500 = {soma}')
