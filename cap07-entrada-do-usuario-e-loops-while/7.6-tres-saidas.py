#  7.6 Três saídas: Crie diferentes versões do Exercício 7.4 ou 7.5 que executem cada uma
#  das seguintes tarefas, pelo menos uma vez:
#  • Use um teste condicional na instrução while para interromper o loop.
#  • Use uma variável active para controlar o tempo que o loop é executado.
#  • Use uma instrução break para sair do loop quando o usuário inserir o valor 'quit'


prompt = "Venda de ingressos, o preço depende da idade\n"
print(prompt)
active = True

while active == True:
    idade = int(input("Digite sua idade: "))
    if idade < 3:
        print("Ingresso gratuíto")
    elif idade >= 3 and idade <= 12:
        print("Ingresso custa U$10")
    else:
        print("Ingresso custa U$15")
    
    #sair = input("Se deseja sair digite quit e pressione enter, caso contrário apenas pressione enter")
    # 1 usando break
    # if sair == 'quit':
    #     break

    # 2 usando teste condicional
    #while sair != 'quit:
    #sair = input("Se deseja sair digite quit e pressione enter, caso contrário apenas pressione enter")

    # 3 usando variavel active
    sair = input("Se deseja sair digite quit e pressione enter, caso contrário apenas pressione enter")
    if sair == 'quit':
        active = False

    

        
