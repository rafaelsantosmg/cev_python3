def maior(*num):
    from time import sleep
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(0.3)
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.3)
    if len(num) == 0:
        print('Não foi informado valor nenhum!')
    else:
        print(f'Foram informados {len(num)} valores ao todo')
        print(f'O maior valor informado foi {max(num)}.')


#  Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
