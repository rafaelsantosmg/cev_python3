"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(*nota, sit=False):
    """
    --> Função para analisar notas e situação de varios alunos.
    :param nota: Recebe varias notas a serem analisadas.
    :param sit: Opcional, mostra a situação dos alunos.
    :return: Mostra o dicionario com todas informações.
    """
    alunos = dict()
    alunos['Total'] = len(nota)
    alunos['Maior nota'] = max(nota)
    alunos['Menor nota'] = min(nota)
    alunos['Média'] = sum(nota) / len(nota)
    if sit:
        if alunos['Média'] < 5:
            alunos['Situação'] = 'RUIM'
        elif 5 >= alunos['Média'] < 7:
            alunos['Situação'] = 'RAZOAVEL'
        else:
            alunos['Situação'] = 'ÓTIMA'
    return alunos


#  Programa Principal
resp = notas(9.5, 7, 6.5, 9, 10, 6, sit=True)
print(resp)
print()
help(notas)
