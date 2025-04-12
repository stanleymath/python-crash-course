#  6.6 Pesquisa: Use o código de favorite_languages.py (página 
# 135).
#  • Crie uma lista de pessoas que deveriam participar da pesquisa de linguagens
#  favoritas. Inclua alguns nomes que já estão no dicionário e outros que não estão.
#  • Percorra com um loop a lista de pessoas que devem participar da pesquisa. Se já
#  tiverem respondido, exiba uma mensagem agradecendo a resposta. Se ainda não
#  tiverem respondido, exiba uma mensagem as convidando a participar.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', 
    }

lista = ('stanley', 'charlie', 'phil', 'edward', 'sarah', 'jen')

for nome in lista:
    if nome in favorite_languages:
        print(f"Obrigado por participar da pesquisa {nome}")
    else:
        print(f"Você gostaria de participar da pesquisa? {nome}")