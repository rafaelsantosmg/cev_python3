"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses
aberto e fechado na ordem correta."""

expr = str(input('Informe sua expressão: ')).strip()
lista =[]
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Você digitou uma expressão VÁLIDA!')
else:
    print('Você digitou uma expressão INVÁLIDA!')
