"""Dentro do pacote utilidadescev que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para
aceitar apenas valores que seja monetários."""
from utilidadescev import dado, moeda

p = dado.leiadinheiro('Digite um preço: R$')
moeda.resumo(p, 10, 5)
