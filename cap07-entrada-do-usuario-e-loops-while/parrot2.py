# permitindo que o usuário encerre um programa

prompt = ("Para encerrar o programa escreva 'quit' e pressione enter: ")

# message = ""
# while message != 'quit':
#     message = input(prompt)
 
#     if message != 'quit':
#         print(message)

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)