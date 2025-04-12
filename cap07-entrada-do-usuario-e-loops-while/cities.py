# usando break pra sair do loop.

prompt = "\nPor favor digite o nome da cidade que quer visitar"
prompt += "\n(Digite 'quit'e pressione enter para finalizar o programa)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(city)