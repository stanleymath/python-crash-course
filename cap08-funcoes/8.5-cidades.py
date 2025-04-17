'''8.5 Cidades: Escreva uma função chamada describe_city() que aceite o nome de uma
 cidade e de seu país. A função deve exibir uma simples frase, como Reykjavik fica na
 Islândia. Forneça ao parâmetro do país um valor default. Chame sua função para três
 cidades diferentes e, pelo menos, para uma que não esteja no país default.'''

def describe_city(cidade, pais='Brasil'):
    return print(f"{cidade} fica no {pais}")

describe_city('Morrinhos')
describe_city('São Paulo')
describe_city('Woshington', 'EUA')



