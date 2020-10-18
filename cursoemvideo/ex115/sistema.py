from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastras', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        escreverArquivo(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do programa... Até logo!')
        sleep(2)
        break
    else:
        print('\033[31mErro! Opção invalida\033[m')
    sleep(1.5)
