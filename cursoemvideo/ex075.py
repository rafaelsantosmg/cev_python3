"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

num = (int(input(f'Digite 1º valor: ')),
       int(input(f'Digite 2º valor: ')),
       int(input(f'Digite 3º valor: ')),
       int(input(f'Digite 4º valor: ')))
print(f'O número 9 aparece {num.count(9)} vezes!')
if 3 in num:
    print(f'O primeiro número 3 digitado apareceu no {num.index(3)+1}º posição.')
else:
    print('O núemero 3 não foi digitado!')
print(f'Os números pares são ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
