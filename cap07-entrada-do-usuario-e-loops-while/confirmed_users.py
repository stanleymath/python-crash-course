# começa com usuarios que precisam ser verificados, e uma lista vazia a fim de armazenar os usuários confirmados.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# faz a verificação de cada usuário até que não se tenha mais
# usuarios nao confirmados
# transfere cada usuario verificado para a lista de usuarios confirmados

while unconfirmed_users:
    unconfirmed_users.reverse()
    current_user = unconfirmed_users.pop()
    
    print(f"Verficando usuário: {current_user.title()}")
    confirmed_users.append(current_user)

# exibe todos os usuários confirmados
print("Os seguintes usuarios foram verificados com sucesso: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())