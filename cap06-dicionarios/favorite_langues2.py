favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    'stanley': ['python'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()} linguagens favoritas são: ")
    else: print(f"\n{name.title()} a linguagem favorita: ")
    for language in languages:
        print(f"{language.title()}")