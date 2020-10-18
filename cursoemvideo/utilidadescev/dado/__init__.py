from utilidadescev.string import cabecalho, linha


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
            num = float(input(msg))
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
            nome = str(input(msg)).strip().title()
        except KeyboardInterrupt:
            print('\n\033[31mFinalizado pelo usuário!\033[m')
            break
        else:
            if len(nome) < 3:
                print('\033[31mDado incorreto!\033[m Informe um Nome válido!')
                nome = ''
                continue
            return nome


def menu(lista, msg='MENU PRINCIPAL'):
    """
    -> Cria um menu com multiplas escolhas.
    :param msg: recebe o título do menu.
    :param lista: recebe uma lista com as informações do menu.
    :return: o valor lido pelo usuário.
    """
    cabeçalho(msg)
    for k, item in enumerate(lista):
        print(f'{k+1} - \033[34m{item}\033[m')
    linha()
    opc = leia_inteiro('\033[33mSua Opção: \033[m')
    return opc
