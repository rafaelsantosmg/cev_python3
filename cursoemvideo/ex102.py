"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que será um valor logico(opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial."""


def fatorial(n, show=False):
    '''
    -->Função para cálculo de Fatorial.
    :param n: Número para calcular o fatorial.
    :param show: Mostra o processo do cálculo quando verdadeiro.
    :return: O resultado do Fatorial de um número.
    '''
    from math import factorial
    print('-' * 60)
    print(f'O fatorial de {n}! = ', end='')
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')
            print(f'x ' if c > 1 else '= ', end='')
    return print(f'{factorial(n)}')


fatorial(5)
print()
help(fatorial)
