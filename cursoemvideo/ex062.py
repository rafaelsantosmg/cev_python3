"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos. """

print('-=-'*14)
print('-'*12, 'TERMOS DE UMA PA', '-'*12)
print('-=-'*14)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
total = 0
count = 1
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print(termo, end=' → ')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'A progressão foi finalizada com {count} termos!')
print('FIM')
