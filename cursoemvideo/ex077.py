"""Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ('abelha', 'caixa', 'livro', 'caderno', 'bexiga', 'colorido', 'carro', 'paralelepipedo', 'helicoptero')
for p in palavras:
    print(f'\nNa palavra \033[1;91m"{p}"\033[m temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiuo':
            print(f'\033[1;91m{letra}\033[m', end=' ')
