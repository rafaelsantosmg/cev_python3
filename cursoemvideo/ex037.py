"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. """

from utilidadescev.dado import menu
from utilidadescev.dado import leiaint
from utilidadescev.string import *

while True:
    linha()
    num = leiaint('Digite um número inteiro: ')
    opcao = menu(['Converter para BINÁRIO', 'Converter para OCTAL', 'Converter para HEXADECIMAL', 'Sair do programa'])
    #  Programa de conversão de números inteiro.
    if opcao == 1:
        linha(50, 'verde')
        print(f'{num} convertido para BINÁRIO é: {bin(num)[2:]}')
    elif opcao == 2:
        linha(50, 'verde')
        print(f'{num} convertido para OCTAL é: {oct(num)[2:]}')
    elif opcao == 3:
        linha(50, 'verde')
        print(f'{num} convertido para HEXADECIMAL é: {hex(num)[2:]}')
    elif opcao == 4:
        linha(50, 'cinza')
        print('PROGRAMA ENCERRADO')
        break
    else:
        linha(50, 'vermelho')
        print('Opção inváçida!')
        continue
