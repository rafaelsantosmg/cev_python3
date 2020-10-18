"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

princ = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        princ[0].append(n)
    else:
        princ[1].append(n)
print('-' * 50)
print(f'Os valores digitados foi {princ}')
print(f'Os valores pares digitados foram {sorted(princ[0])}')
print(f'Os valores ímpares digitados foram {sorted(princ[1])}')
