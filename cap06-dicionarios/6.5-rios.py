#  6.5 Rios: Crie um dicionário contendo os três principais rios e o país por onde cada rio
#  passa. Um par chave-valor pode ser 'nile': 'egypt'.
#  • Use um loop para exibir uma frase sobre cada rio, como: O Nilo atravessa o Egito.
#  • Use um loop para exibir o nome de cada rio incluído no dicionário.
#  • Use um loop para exibir o nome de cada país incluído no dicionário.

rios = {
    'nilo':
    'Egito',
    'jordão':
    'Israel',
    'amazonas':
    'Brasil',
}

# exibindo rio e pais
for rio, pais in rios.items():
    if pais == 'Israel':
        print(f"O {rio} atravessa {pais}")
    else:
        print(f"O {rio} atravessa o {pais}")

# exibindo somente rio
for rio in rios.keys():
    print(rio)

# exibindo somente pais
for pais in rios.values():
    print(pais)