#  6.8 Animais de estimação: Crie vários dicionários, em que cada dicionário representa
#  um animal de estimação diferente. Em cada dicionário inclua o tipo de animal e o nome
#  do dono. Armazene esses dicionários em uma lista chamada pets. Depois, percorra sua
#  lista com um loop e, enquanto faz isso, exiba tudo o que sabe sobre cada animal de
#  estimação.

animal_estimacao1 = {
    'animal': 'cachorro',
    'dono': 'stan'
    }

animal_estimacao2 = {
    'animal': 'gato',
    'dono': 'amanda'
    }

animal_estimacao3 = {
    'animal': 'papagaio',
    'dono': 'luana'
    }

animal_estimacao4 = {
    'animal': 'onça',
    'dono': 'stefan'
    }

animal_estimacao5 = {
    'animal': 'macaco',
    'dono': 'marcia'
    }

animal_estimacao6 = {
    'animal': 'cachorro',
    'dono': 'stan'
    }

# se caso fosse inumeros dicionarios
pets = []

# A função acessa variaveis dinamicamente pelo nome
for i in range(1,7):
    pets.append(globals()[f"animal_estimacao{i}"])

for animal in pets:
    print(f"\n animal: {animal['animal']}\n dono: {animal['dono']}")