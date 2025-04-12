#  7.4 Ingredientes de pizza: Escreva um loop que solicite ao usuário uma série de
#  ingredientes de pizza até que ele forneça o valor 'quit'. À medida que cada ingrediente
#  é fornecido, exiba uma mensagem informando que esses ingredientes estão sendo
#  adicionados à pizza..

prompt = "Digite os ingredientes que deseja adicionar na pizza: "
prompt += "\nQuando adicionar todos digite 'finalizar' para concluir sua pizza"

while True:
    ingrediente = input("Digite o ingrediente: ")
    if ingrediente != 'finalizar':
        print(f"O ingrediente {ingrediente.title()} foi adicionado na sua pizza!")
    else:
        print(f"Pizza finalizada, indo para preparo!")
