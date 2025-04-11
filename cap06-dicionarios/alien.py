alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


# dicionário mais simples tem exatamente um par chave-valor, como por exemplo:
#Acessando valor o valor da chave
alien_0 = {'color': 'green'}
print(alien_0['color'])

#dicionário com dois pares chave-valor:
alien_0 = {'color': 'green', 'point': 5}

alien_0 = {'color': 'green', 'points': 5}

novos_pontos = alien_0['points']
print(f"Você acabou de ganhar {novos_pontos} pontos!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#começando com um dicionário vazio
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#modificando valores em um dicionário
alien_0 = {'color': 'green'}
print(f"O alien é {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"O alien agora é {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Posição original: {alien_0['x_position']}")