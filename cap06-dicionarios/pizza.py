# uma lista em um dicionário

# armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Resume o pedido
print(f"Você pediu uma pizza com borda {pizza['crust']} com os seguintes ingredientes")
for topping in pizza['toppings']:
    print(f"\t{topping}")

