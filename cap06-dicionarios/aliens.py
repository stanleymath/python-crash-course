alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Um exemplo mais realista seria mais de três alienígenas em código
 #que gere automaticamente cada alienígena.

# cria uma lista vazia para armazenar aliens
aliens = []

# cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

# exibe os 5 primeiros alienigenas
for alien in aliens[:5]:
    print(alien)
print("...")

# exibem quantos alienigenas foram criados
print(f"Numero total de aliens criados: {len(aliens)}")

# modificando os alienigenas

aliens = []

# cria 30 aliens verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

# Exibe os primeiros 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")