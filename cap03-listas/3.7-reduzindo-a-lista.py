convidades = ['Albert Einstein', 'Stephen Hawking', 'Marie Curie']

message = f"Olá nobre senhor. Aqui falas apenas um estudante bagre, está afim de um janta? -Gostaria muito de vos ouvilos falar sobre os conhecimentos que possuem. Para: {convidades[0]}, {convidades[1]} e {convidades[2]}"

print(message)

print(f"{convidades[0]} não irá ao jantar")

del convidades[0]

convidades.insert(0, 'Heisenberg')
print(convidades)

print(f"Olá, {convidades}, encontrei uma mesa maior e vou convidar os carinhas da quântica para a conversa ficar mais interessante")

convidades.insert(0, 'Schrodinger')
convidades.insert(2, 'Hartree')
convidades.append('Max planck')

print(convidades)

print("Moio e há apenas uma mesa para 3 pessoas, eu e mais 2 convidados. Nesse caso retirarei o convite")

convidado1 = convidades.pop(0)
print(f"{convidado1} não irá")
convidado2 = convidades.pop(1)
print(f"{convidado2} não irá")
convidado3 = convidades.pop(2)
print(f"{convidado3} não irá")
convidado4 = convidades.pop(2)
print(f"{convidado4} não irá")


print(convidades)

print(f"Agora só irá comigo os carinhas da quântica =D {convidades}")

