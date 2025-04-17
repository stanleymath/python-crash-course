# começa com alguns designs que precisam ser impressos.

def print_models(unprinted_designs, completed_models):
    '''Simula a impressão de cada design, até que não reste nenhum.
    passa cada design para compelted_models após impressão'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''Exibe todos os modelos impressos'''
    print("\nThe followiing models have been printed:")
    for completed_model in completed_models:
        print(completed_models)

unprinted_designs = ['phone case', 'rebot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)


