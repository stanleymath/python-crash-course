''' 8.15 Imprimindo modelos: Insira as funções do exemplo printing_models.py em um
 arquivo separado chamado printing_functions.py. Escreva uma instrução import na
 parte superior do printing_models.py e modifique o arquivo para usar as funções
 importadas.'''

import printing_functions as p

unprinted_designs = ['phone case', 'rebot pendant', 'dodecahedron']
completed_models = []

p.print_models(unprinted_designs, completed_models)
p.show_completed_models(completed_models)