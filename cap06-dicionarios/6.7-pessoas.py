#  6.7 Pessoas: comece com o programa escrito para Exercício 6.1 (página 
# 138). Crie dois
#  dicionários novos representando pessoas diferentes e armazene todos os três
#  dicionários em uma lista chamada people. Percorra sua lista de pessoas com um loop. À
#  medida que percorre a lista, exiba tudo o que sabe sobre cada pessoa.

# 

info_pessoa1 = {
    'nome':
    'Ana',
    'Sobrenome':
    'Lucas',
    'idade':
    '28',
    'cidade':
    'Morrinhos'
    }

info_pessoa2 = {
    'nome':
    'stan',
    'Sobrenome':
    'math',
    'idade':
    '27',
    'cidade':
    'Morrinhos'
}

info_pessoa3 = {
    'nome':
    'amanda',
    'Sobrenome':
    'silva',
    'idade':
    '20',
    'cidade':
    'caldas-novas'
}

people = (info_pessoa1, info_pessoa2, info_pessoa3)

for pessoa in people:
    print(f"\nNome da pessoa:  {pessoa['nome']} {pessoa['Sobrenome']}\nIdade: {pessoa['idade']}\nCidade: {pessoa['cidade']}")
