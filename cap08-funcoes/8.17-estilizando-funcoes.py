'''8.17 Estilizando funções: Escolha os três programas que você escreveu para este
 capítulo e garanta que sigam as diretrizes de estilo descritas nesta seção'''


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

def info_carro(fabricante, modelo, **args):
    '''Recebe as informações sobre o veículo e as imprime'''
    args['fabricante'] = fabricante
    args['modelo'] = modelo
    print(args)

def make_album(artista, titulo):
    '''Preenche o dicionário album e retorna as informações'''
    album = {
        'artista': artista,
        'titulo': titulo
    }

    return album