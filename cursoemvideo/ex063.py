"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8 """

print('=*'*26)
print('*'*14, 'SEQUENCIA DE FIBONACCI', '*'*14)
print('=*'*26)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = 0
c = 3
print('{} → {}'.format(t1, t2), end='')
while c < n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
