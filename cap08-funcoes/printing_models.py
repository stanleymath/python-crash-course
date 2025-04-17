# começa com alguns designs que precisam ser impressos.

unprinted_designs = ['phone case', 'rebot pendant', 'dodecahedron']
completed_models = []

# simula a impressão de cada design, até que não reste nenhum
# passa cada design para completed_models após impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# exibe todos os modelos concluídos
print("\n The following models have been printed: ")
for completed_model in completed_models:
    print(completed_models)