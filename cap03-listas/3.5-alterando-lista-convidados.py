convidades = ['Albert Einstein', 'Stephen Hawking', 'Marie Curie']

message = f"Olá nobre senhor. Aqui falas apenas um estudante bagre, está afim de um janta? -Gostaria muito de vos ouvilos falar sobre os conhecimentos que possuem. Para: {convidades[0]}, {convidades[1]} e {convidades[2]}"

print(message)

print(f"{convidades[0]} não irá ao jantar")

del convidades[0]

convidades.insert(0, 'Heisenberg')
print(convidades)