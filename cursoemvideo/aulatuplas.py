lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(lanche)
print()
for comida in lanche:  # mostra os itens da variavel seguindo a ordem dos blocos [0:...]
    print(f'Eu comi {comida}')
print()
for cont in range(0, len(lanche)):  # mostra os itens da variavel e a posição dentro de cada bloco
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print()
for pos, comida in enumerate(lanche):  # define a variavel para o comando enumerate e mostra os itens da variavel e a
    # posição dentro de cada bloco
    print(f'Eu vou comer {comida} na posição {pos}')
print()
print('Cara comi demais!')
print()
print(sorted(lanche))  # Ordena os itens da variável

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # soma a tupla a + b, nota que os valores são agregados e não somados
d = b + a  # soma a tupla b + a, nota que os valores são agregados e não somados
print(a)
print(b)
print(c)
print(d)
print(c.count(5))  # metodo count mostra quantas x '5' aparece na tupla
print(c.index(4))  # metodo index mostra a posição que foi encontrado o primeiro '4'
