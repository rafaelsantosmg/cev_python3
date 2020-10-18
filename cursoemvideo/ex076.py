"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados m forma tabular."""

produtos = ('Acucar', '8,60', 'Feijão', '10,20', 'Arroz', '19,00', 'Macarrão', '6,50', 'Nescal', '11,90',
            'Detergente', '3,40', 'Molho de tomate', '1,99')
print('*' * 40)
print('{:-^40}'.format('LISTA DE PREÇO'))
print('*' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='R$ ')
    elif pos % 2 == 1:
        print(f'{produtos[pos]:30}')
print('*' * 40)
