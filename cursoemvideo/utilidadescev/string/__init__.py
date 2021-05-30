from cursoemvideo.utilidadescev.dado import leia_inteiro


def cores(valor):
    """
    -> Coloca cor nas linhas e cabeçalhos.
    :param valor: recebe a cor por extenso.
    :return: a cor.
    """
    cor = {'preto': '\033[1;97m',
           'vermelho': '\033[1;91m',
           'verde': '\033[1;92m',
           'amarelo': '\033[1;93m',
           'azul': '\033[1;94m',
           'magenta': '\033[1;95m',
           'cinza': '\033[1;96m',
           'limpa': '\033[m'}
    return cor[valor]


def linha(tam=50, cor="limpa", lin='-'):
    """
    -> Função escreve linha e preenche com o parâmetro (lin) atribuido.
    :param tam: recebe o tamanho da linha a ser escrita.
    :param cor: recebe a cor da linha.
    :param lin: recebe o tipo da linha, ex:('-', '=', '*', '_'...).
    :return: linha formatada.
    """
    return print(f'{cores(cor)}{lin * tam}')


def cabecalho(msg, tam=50, cor="limpa", lin='-', formatacao=' '):
    """
    -> Função Cabeçalho personalizado.
    :param msg: recebe uma mensagem e centraliza.
    :param tam: define o tamanho da linha.
    :param cor: define a cor de exibição do cabeçalho e das linhas presentes na função.
    :param lin: define o tipo de linha a ser exibido separando a mensagem, ex:('-', '='...).
    :param formatacao: define uma formatação entre a mensagem, ex:('*' **** mgs ****).
    :return: a mensagem como cabeçalho formatado.
    """
    while True:
        validador = False
        comp = len(lin)
        validador = lin.isalnum()
        if validador:
            print(f'Parâmetro "{lin}" inválido!')
            break
        if comp >= 2:
            print(f'\033[1;31m]Parâmetro \033[m"{lin}" \033[1;31m]inválido!\033[m '
                  f'Digite apenas um valor no campo linha.')
            break
        else:
            linha(tam, cor, lin)
            print(f'{cores(cor)}{msg.center(tam, formatacao)}{cores("limpa")}')
            linha(tam, cor, lin)
        break


def menu(lista, msg='MENU PRINCIPAL'):
    """
    -> Cria um menu com multiplas escolhas.
    :param msg: recebe o título do menu.
    :param lista: recebe uma lista com as informações do menu.
    :return: o valor lido pelo usuário.
    """
    cabecalho(msg)
    for k, item in enumerate(lista):
        print(f'{k+1} - \033[34m{item}\033[m')
    linha()
    opc = leia_inteiro('\033[33mSua Opção: \033[m')
    return opc
