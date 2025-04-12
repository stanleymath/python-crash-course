# 6.2 Números favoritos: Use um dicionário para armazenar os números favoritos das
#  pessoas. Pense em cinco nomes e os utilize como chaves em seu dicionário. Pense em
#  um número favorito para cada pessoa e armazene cada um como um valor em seu
#  dicionário. Exiba o nome de cada pessoa e seu número favorito. Para que tudo fique
#  ainda mais divertido, pergunte a alguns amigos e obtenha alguns dados reais para o
#  seu programa.

num_favoritos = {
    'Stanley':
    '5',
    'Charlie':
    '35',
    'Melanie':
    '27',
    'Chucky':
    '30',
    'Ben':
    '10',
    }

for num_pessoas in num_favoritos:
    print(f"O número favorito de {num_pessoas} é {num_favoritos[num_pessoas]}")