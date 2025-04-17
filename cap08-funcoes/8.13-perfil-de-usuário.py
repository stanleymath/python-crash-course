'''8.13 Perfil de usuário: Comece com uma cópia do user_profile.py da página 
194. Crie
 um perfil de si mesmo chamando build_profile(), com seu primeiro nome e sobrenome
 e três outros pares chave-valor que o representem.'''

def build_profile(first, last, **user_info):
    '''Cria um dicionário contendo tudo o que sabemos sobre um usuário'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('stanley', 'matheus',
                             location='matheus',
                             field='químico',
                             new_field='tecnologia')
print(user_profile)