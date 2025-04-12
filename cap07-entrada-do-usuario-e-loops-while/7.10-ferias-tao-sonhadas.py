# 7.10 Férias tão sonhadas: Crie uma pesquisa que pergunte aos usuários sobre as férias
#  de seus sonhos. Crie um prompt mais ou menos assim: Se pudesse visitar qualquer
#  lugar do mundo, para onde iria? Inclua um bloco de código que exiba os resultados
#  dessa pesquisa.

prompt = "Se pudesse visitar qualquer lugar do mundo para onde iria? "
pesquisa = {}

while True:
    nome = input("Qual seu nome? ")
    lugares = input(prompt)
    pesquisa[nome] = lugares

    print("Resultados da pesquisa!")
    for nome, lugar in pesquisa.items():
        print(f"{nome}: {lugar}")

    exec = input("Deseja prosseguir com a pesquisa? (n/s)")
    if exec == 'n':
        break
    