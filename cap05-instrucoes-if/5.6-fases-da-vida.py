#  5.6 Fases da vida: Escreva uma sequência if-elif-else que determine a fase da vida de
#  uma pessoa. Defina um valor para a variável age, e depois:
#  • Se a pessoa tiver menos de 2 anos, exiba uma mensagem informando que a pessoa
#  é um neném.
# • Se a pessoa tiver pelo menos 2 anos, e menos de 4, exiba uma mensagem
#  informando que é uma criança.
#  • Se a pessoa tiver pelo menos 4 anos, e menos de 13, exiba uma mensagem
#  informando que é um(a) garoto(a).
#  • Se a pessoa tiver pelo menos 13 anos, e menos de 20, exiba uma mensagem
#  informando que é adolescente.
#  • Se a pessoa tiver pelo menos 20 anos, e menos de 65, exiba uma mensagem
#  informando que é um adulto.
#  • Se a pessoa tiver 65 anos ou mais, imprima uma mensagem informando que a
#  pessoa é um(a) idoso(a).

age = 27

if age < 2:
    print("Você é um neném")
elif age >= 2 and age <= 4:
    print("Você é uma criança")
elif age >= 13 and age <= 20:
    print("Você é um adolescente")
elif age >= 20 and age <= 65:
    print("Você é um adulto")
else: 
    print("Você é um idoso")