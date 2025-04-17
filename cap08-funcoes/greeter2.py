def get_formatted_name(first_name, last_name):
    '''Retorna um nome compelto, formatado elegantemente'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()

# Temos um loop infinito aqui!
while True:
    print("\nPlease tell me your name: ")
    print("(entender 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")

    
    get_formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {get_formatted_name}!")