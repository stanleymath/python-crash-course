#  4.11 Minhas pizzas, suas pizzas: Comece com o programa do Exercício 4.1 (página 
# • Adicione uma pizza nova à lista original.
#  90).
#  Faça uma cópia da lista de pizzas e a nomeie como friend_pizzas. Em seguida, siga as
#  etapas:
#  • Adicione uma pizza diferente à lista friend_pizzas.
#  • Prove que tem duas listas separadas. Exiba a mensagem: Minhas pizzas favoritas
#  são:. E, em seguida, use um loop for para exibir a primeira lista. Exiba a mensagem:
#  Minhas pizzas favoritas são:. E, em seguida, use um loop for para exibir a segunda
#  lista. Garanta que cada pizza nova seja armazenada na lista adequada.

pizzas = ['Calabresa', 'Mussarela', '3 Queijos']

friend_pizzas = pizzas[:]

pizzas.append('Portuguesa')

friend_pizzas.append('Metade mussarela Metade Calabresa')

print(f"Minhas pizzas favoritas são:")

for pizza in pizzas:
    print(pizza)

print(f"As pizzas favoritas dos meus amigos são:")

for pizza in friend_pizzas:
    print(pizza)
      
