#  4.12 Mais loops: Nesta seção, todas as versões de food.py evitaram o uso de loops for
# para exibição, a fim de economizar espaço. Escolha uma versão de food.py e escreva
#  dois loops for para exibir cada lista de alimentos.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("Minhas comidas favoritas")
for food in my_foods:
    print(food)

print("\nAs comidas favoritas dos meus amigos")
for food in friend_foods:
    print(food)