""" Escreva um programa que leia nome, idade e sexo de 4 pessoas.
No final do programa mostre:
A média de idade do grupo.
Qual o nome do homem mais velho.
quantas mulheres têm menos de 20 anos. """

media = 0
maisvelho = 0
feminino = 0
novas = 0
nomemaisvelho = ''
for c in range(1, 5):
    print('-='*25)
    nome = str(input(f'Informe o NOME da {c}ª pessoa: ')).upper().strip()
    idade = int(input('Informe a IDADE: '))
    sexo = str(input('Informe o SEXO [F/M]: ')).strip().upper()
    media += idade / 4
    if sexo == 'F':
        feminino += 1
        if idade < 20:
            novas += 1
    else:
        if c == 1:
            maisvelho = idade
            nomemaisvelho = nome
        if idade > maisvelho:
            maisvelho = idade
            nomemaisvelho = nome
print('-='*25)
print(f'A media da idade entre eles foram {round(media)}')
print(f'O homem mais velho do grupo tem {maisvelho} e se chama {nomemaisvelho}')
print(f'{novas} mulheres tem menos de 20 anos!')
