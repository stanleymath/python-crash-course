# 

current_users = ['admin', 'joao', 'MARIA', 'carlos', 'ana', 'Amanda']

new_users = ['joao', 'MARIA', 'mariana', 'beatriz', 'susane', 'admin', 'amanda']

#cria lista vazia para introduzir upper() e title()
current_upper_users = []
current_title_users = []

#introduz os users da lista current_users em upper()
for user in current_users:
    current_upper_users.append(user.upper())

for user in current_users:
    current_title_users.append(user.title())

#verificações 
for users in new_users:
    if users in current_users:
       print(f"Nome de usuário: {users} em uso")
    elif users.upper() in current_upper_users:
       print(f"Nome de usuário: {users.upper()} em uso")
    elif user.title() in current_title_users:
       print(f"Nome de usuário: {users.title()} em uso")
    else:
        print(f"Nome de usuário:{users} disponível")