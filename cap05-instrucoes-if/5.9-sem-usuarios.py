#  5.9 Sem usuários: adicione um teste if a hello_admin.py a fim de garantir que a lista de
#  usuários não esteja vazia.
#  • Se a lista estiver vazia, exiba mensagem: É necessário encontrar alguns usuários!
#  • Remova todos os nomes de usuários de sua lista e verifique se a mensagem correta
#  foi exibida.

# Arquivo: hello_admin.py

usuarios = ['admin', 'joao', 'maria', 'carlos', 'ana']

# Removendo todos os usuários da lista para testar a verificação
usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print("Olá admin, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {usuario}, obrigado por fazer login novamente.")
else:
    print("É necessário encontrar alguns usuários!")

