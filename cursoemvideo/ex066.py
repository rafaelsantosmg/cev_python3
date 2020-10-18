"""Crie um programa que leia vários números inteiro pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, o que é a
condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag 999)"""

soma = count = 0
while True:
    num = int(input('Digite um valor, para parar 999: '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'Você digitou {count} números e a soma dos valores são: {soma}')
