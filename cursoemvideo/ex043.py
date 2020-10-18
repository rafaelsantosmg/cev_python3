"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do peso.
de 18.5 a 25: Peso ideal.
de 25 a 30: Sobrepeso.
de 30 a 40: Obesidade
acima de 40: Obesidade morbida."""

from utilidadescev.dado import leiafloat
from utilidadescev.string import linha

#  Indice de massa corporal
linha(60, 'cinza')
peso = leiafloat('Entre com seu peso: ')
altura = leiafloat('Entre com sua altura: ')
linha(60, 'cinza')
imc = peso / altura ** 2
linha(60, 'verde')
print(f'O IMC dessa pessoa é {imc:.1f} ', end='')
if imc <= 18.5:
    print('Essa pessoa está ABAIXO DO PESO!')
elif imc <=25:
    print('Essa pessoa está no PESO IDEAL!')
elif imc <=30:
    print('Essa pessoa está com SOBREPESO!')
elif imc <=40:
    print('Essa pessoa está com OBESIDADE!')
else:
    print('Essa pessoa está com OBESIDADE MORBIDA!')
linha(60, 'verde')
