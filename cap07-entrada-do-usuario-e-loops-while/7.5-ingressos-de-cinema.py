#  7.5 Ingressos de cinema: Um cinema cobra preços de ingressos diferentes, dependendo
#  da idade da pessoa. Se a pessoa for menor de 3 anos, o ingresso é gratuito; se tiver
#  entre 3 e 12 anos, o ingresso custa U$S10; e caso tenha mais de 12 anos, o ingresso
#  custa US$15. Escreva um loop que pergunte a idade dos usuários e, em seguida,
#  informe o preço do ingresso do cinema..


prompt = "Venda de ingressos, o preço depende da idade\n"
print(prompt)

while True:
    idade = int(input("Digite sua idade: "))
    if idade < 3:
        print("Ingresso gratuíto")
    elif idade >= 3 and idade <= 12:
        print("Ingresso custa U$10")
    else:
        print("Ingresso custa U$15")
    
