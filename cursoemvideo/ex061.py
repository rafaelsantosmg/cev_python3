"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while."""

print('-=-'*14)
print('-'*10, '10 TERMOS DE UMA PA', '-'*11)
print('-=-'*14)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
c = 0
while c <= 10:
    print(termo, end=' → ')
    termo += razao
    c += 1
print('Acabou')
