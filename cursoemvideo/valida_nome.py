while True:
    nome = list()
    entrada = str(input('Digite seu Nome: ')).strip().title()
    temp = entrada.split()
    c = 1
    n = 0
    for v in temp:
        if v.isalpha():
            if c == 1:
                if len(v) <= 3:
                    print('ERRO! Nome Inválido! Digite um Nome com mais de 3 letras!')
                    c = 1
                    nome = list()
                    n = 1
                    continue
                c += 1
            nome.append(v)
        else:
            print('ERRO! Nome não pode conter números!')
            nome = list()
            n = 1
            continue
    for v in nome:
        nome_completo = v
        n += 1
        print(nome_completo, end=' ')
    if n == len(nome):
        break
