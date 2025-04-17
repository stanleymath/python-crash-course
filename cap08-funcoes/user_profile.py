def build_profile(first, last, **user_info):
    '''Cria um dicionário contendo tudo o que sabemos sobre um usuário'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)