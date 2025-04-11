recheios_solicitados = []

if recheios_solicitados:
    for recheio in recheios_solicitados:
        print(f"Adicionando {recheio}")
    print("\nFinalizado o preparo da sua pizza.")
else:
    print("Tem certeza de que quer uma pizza simples?")

# Usando múltiplas listas
recheios_disponiveis = ['cogumelos', 'azeitonas', 'pimentões verdes', 'pepperoni', 'abacaxi', 'queijo extra']

recheios_solicitados = ['cogumelos', 'batata frita', 'queijo extra']

for recheios_solicitado in recheios_solicitados:
    if recheios_solicitado in recheios_solicitados:
        print(f"Adicionando {recheios_solicitado}")
    else:
        print(f"Desculpe, nós não temos {recheios_solicitado}")

print("\nSua pizza está pronta")