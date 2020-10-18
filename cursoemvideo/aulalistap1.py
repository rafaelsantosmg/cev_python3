num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.insert(2, 2)
num.remove(1)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(1, 6):
    valores.append(int(input(f'Digite {cont}º valor')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fonal da lista.')

'''a = [2, 3, 4, 7]
b = a  # esse metodo cria uma ligação entre elas
b = a[:]  # esse método faz uma copia "a" em "b"
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
