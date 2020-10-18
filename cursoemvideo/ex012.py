'''Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
preco = float(input('Preço do produto R$'))
desc = preco * 5 / 100
print(f'O valor do produto com 5% de desconto fica R${preco - desc:.2f}')
