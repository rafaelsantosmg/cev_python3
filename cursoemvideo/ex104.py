"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""


def leiaint(txt):
    while True:
        n = str(input(txt)).strip()
        if not n.isnumeric():
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            int(n)
            break
    return n


#  Programa Principal
n = leiaint('Digite um número: ')
print(f'O número digitado foi {n}.')
