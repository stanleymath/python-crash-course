''' 8.6 Nome de cidades: Escreva uma função chamada city_country() que recebe o nome
 de uma cidade e seu país. A função deve retornar uma string formatada como esta:
 "Santiago, Chile"
 Chame sua função com pelo menos três pares cidade-país e exiba os valores
 retornados.'''

def city_country(cidade, pais):
    return f"{cidade.title()}, {pais.title()}"

print(city_country('Morrinhos', 'Brasil'))
print(city_country('são paulo', 'Brasil'))
print(city_country('maringa', 'brasil'))
