alien_0 = {'color': 'green', 'speed': 'slow'}
# retorna erro pois nao existe a chave print(alien_0['points'])

#utilizamos o método get() para evitar erros e checar se existe a chave
point_value = alien_0.get('points', 'Nao existe a chave points')
print(point_value)


