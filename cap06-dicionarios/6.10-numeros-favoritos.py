# 6.2 Números favoritos: Use um dicionário para armazenar os números favoritos das
#  pessoas. Pense em cinco nomes e os utilize como chaves em seu dicionário. Pense em
#  um número favorito para cada pessoa e armazene cada um como um valor em seu
#  dicionário. Exiba o nome de cada pessoa e seu número favorito. Para que tudo fique
#  ainda mais divertido, pergunte a alguns amigos e obtenha alguns dados reais para o
#  seu programa.

num_favoritos = {
    'Stanley': [5, 10, 15, 1997],
    'Charlie': [3, 18, 26],
    'Melanie': [9, 12, 19],
    'Chucky': [24, 13, 19],
    'Ben': [34, 12, 29, 33],
    }

for nome, numeros in num_favoritos.items():
    print(f"\nOs números favoritos de {nome.title()} são: ")

    for numero in numeros:
        print(numero)


