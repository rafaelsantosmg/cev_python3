"""Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenção de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
mostra-lo por extenso."""

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vite')
num = int(input('Digite um número de 0 a 20: '))
while num not in range(0, 21):
        num = int(input('Número invalido! Digite um número de 0 a 20: '))
print(f'Você digitou o número {extenso[num]}')
