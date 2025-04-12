responses = {}

# define uma flag para sinalizar que a pesquisa está ativa
polling_active = True

while polling_active:
    # solicita o nome e a resposta do participanter
    name = input("\nQual seu nome?")
    response = input("Qual montanha você gostaria de escalar algum dia?")

    # armazena a resposta no dicionário
    responses[name] = response
    
    #detecta se mais alguém partipará da pesquisa
    repeat = input("Você gostaria de deixar outra pessoa responder?(no/sim)")
    if repeat == 'no':
        polling_active = False
    
    # A pesquisa está completa. Mostra os resultados.
    print("\nResultado da pesquisa")
    for name, response in responses.items():
        print(f"{name} como respondeu {response}")