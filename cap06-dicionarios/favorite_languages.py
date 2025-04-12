favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"A linguagem favorita da Sarah é {language}")

#acessa chave e valor
for k,v in favorite_languages.items():
    print(f"\n A linguagem favorita de {k.title()} é {v}")

for name in favorite_languages.keys():
    print(f"Retorna somente a chave: {name}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', 
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Oi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()} Eu vejo seu amor pela linguagem{language}!")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', 
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, por favor, participe")

#Percorrendo as chaves de um dicionário com um loop em uma ordem específica

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', 
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, obrigado por responder a pergunta!")
    
# percorrendo todos os valores de um dicionário com um loop

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', 
    }

print("Apenas as linguagens serão mencionadas")
for language in favorite_languages.values():
    print(language.title())

# percorrendo os valores sem repetir caso ouver repetidos

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', 
    }

print("Apenas as linguagens serão mencionadas")
for language in set(favorite_languages.values()):
    print(language.title())


# conjunto em python

languages = {'python', 'rust', 'python', 'c'}
print(languages)