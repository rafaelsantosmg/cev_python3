def metade(preco=0, formatação=False):
    """
    -> Calcula a metade do preço informado.
    :param preco: o preço que quer reajustar.
    :param formatação: saida formatada (opcional).
    :return: o valor reajustado com ou sem formatação.
    """
    res = preco / 2
    return res if formatação is False else moeda(res)


def dobro(preco=0, formatação=False):
    """
    -> Calcula o dobro do preço informado.
    :param preco: preço a ser reajustado.
    :param formatação: saida formatada (opcional).
    :return: o preço reajustado, com ou sem formatação.
    """
    res = preco * 2
    return res if formatação is False else moeda(res)


def aumentar(preco=0, taxa=0, formatação=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param taxa: porcentagem do valor a ser calculado.
    :param preco: o preço que quer reajustar.
    :param formatação: saida formatada (opcional).
    :return: o valor reajustado com ou sem formatação.
    """
    res = preco + (preco * taxa / 100)
    return res if formatação is False else moeda(res)


def diminuir(preco=0, taxa=0, formatação=False):
    """
    -> Calcula o desconto de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param taxa: porcentagem do valor a ser calculado.
    :param preco: o preço que quer reajustar.
    :param formatação: saida formatada (opcional).
    :return: o valor reajustado com ou sem formatação.
    """
    res = preco - (preco * taxa / 100)
    return res if formatação is False else moeda(res)


def moeda(preco=0, valor='R$'):
    """
    -> Faz a conversão do número real para moeda R$.
    :param preco: preço a ser convertido.
    :param valor: definida como padrão para o Real Brasileiro.
    :return: retorna o preço formatado no Real Brasileiro.
    """
    return f'{valor}{preco:.2f}'.replace('.', ',')


def resumo(preco, taxa_maior, taxa_menor):
    """
    -> Formata o preço e as taxas de aumento e desconto,
    e retorna uma visualização tabulado.
    :param preco: preço a ser analisado.
    :param taxa_maior: taxa de aumento em %.
    :param taxa_menor: taxa de desconto em %
    """
    print('-=' * 20)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-=' * 20)
    print(f' Preço analisado: \t\t{moeda(preco)}')
    print(f' Metade do preço: \t\t{metade(preco, True)}')
    print(f' Dobro do preço: \t\t{dobro(preco, True)}')
    print(f' {taxa_maior}% de aumento: \t\t{aumentar(preco, taxa_maior, True)}')
    print(f' {taxa_menor}% de desconto: \t\t{diminuir(preco, taxa_menor, True)}')
    print('-=' * 20)


def compra_dolar(valor):
    while True:
        try:
            valor = float(valor)
            dolar = 5.49
            valor /= dolar
        except (ValueError, TypeError):
            print('\033[1;31mValor inválido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mPrograma interrompido pelo usuário\033[m!')
            break
        else:
            return f'USS{valor:.2f} dólares'
