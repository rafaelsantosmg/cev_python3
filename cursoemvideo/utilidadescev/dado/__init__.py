def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! "{entrada}" não é um preço válido.\033[m')
        else:
            valido = True
            return float(entrada)


def leia_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite apenas números inteiros.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mDados não informado!\033[m')
            return None
        else:
            return num


def leia_real(msg):
    while True:
        try:
            entrada = str(input(msg)).strip().replace(',', '.')
            num = float(entrada)
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite apenas números inteiros ou reais.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mDados não informado!\033[m')
            return None
        else:
            return num


def leia_nome(msg):
    while True:
        try:
            nome = list()
            entrada = str(input('Digite seu Nome: ')).strip().title()
            if entrada == '':
                continue
        except ValueError:
            continue
        except KeyboardInterrupt:
            print('\n\033[31mFinalizado pelo usuário!\033[m')
            return None
        else:
            temp = entrada.split()
            c = 1
            n = 0
            nome_completo = ''
            for v in temp:
                if v.isalpha():
                    if c == 1:
                        if len(v) <= 3:
                            print('\033[31mERRO! Nome Inválido! Digite um Nome com mais de 3 letras!\033[m')
                            c = 1
                            nome = list()
                            n = 1
                            continue
                        c += 1
                    nome.append(v)
                else:
                    print('\033[31mERRO! Nome não pode conter números!\033[m')
                    nome = list()
                    n = 1
                    continue
            for v in nome:
                nome_completo += v + ' '
                n += 1
            if n == len(nome):
                return nome_completo
