"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""

from utilidadescev.dado import leiafloat
from utilidadescev.string import linha
from utilidadescev.numero import media

linha(50, 'magenta')
nota1 = leiafloat('Primeira nota: ')
nota2 = leiafloat('Segunda nota: ')
linha(50, 'magenta')
linha(50, 'cinza')
media = media(nota1, nota2)
print(f'Tirando {nota1} + {nota2} sua média é {media}!')
if media < 5:
    print(f'Sua média foi {media} você está \033[1;31mREPROVADO!\033[0m')
elif media == 5.0 or media < 7:
    print(f'Sua média foi {media} você está de \033[1;33mRECUPERAÇÃO!\033[0m')
elif media >= 7:
    print(f'Sua média foi {media} você está \033[1;32mAPROVADO!\033[0m')
linha(50, 'cinza')
