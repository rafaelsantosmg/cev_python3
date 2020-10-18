"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
ja na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela."""

num = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print(f'O valor foi adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'O valor foi adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-*' * 30)
print(f'Os valores digitados em ordem foram {num}')
