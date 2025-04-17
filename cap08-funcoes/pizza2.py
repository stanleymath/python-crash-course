# importando um módulo inteiro

def make_pizza(size, *toppings):
    '''Sintetiza a pizza que estamos prestes a fazer'''
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
