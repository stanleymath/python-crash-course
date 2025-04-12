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
print(f"Posição atual em y {alien_0['y_position']}")
# Desloca o alienígena para direita
#  Estipula a distância que o alienígena deve percorrer conforme sua velocidade

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Com isso, o alienígena fica veloz
    x_increment = 3

# A posição nova é a posição antiga mais o incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Nova posição: {alien_0['x_position']}")

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Com isso, o alienígena fica veloz
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"A nova posição {alien_0['x_position']}")


#Removendo pares chave-valor

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# o valor é removido de maneira permanente




