def describe_pet(pet_name,animal_type='cachorro'):
    '''Exibe as informações sobre um animal de estimação'''
    print(f"\nEu tenho um {animal_type.title()}.")
    print(f"Meu {animal_type} se chama {pet_name.title()}")

# describe_pet('hamster', 'harry')
# describe_pet('cachorro', 'willie')

# argumentos nomeados: par nome-valor

describe_pet(pet_name='harry')
describe_pet(pet_name='willie')