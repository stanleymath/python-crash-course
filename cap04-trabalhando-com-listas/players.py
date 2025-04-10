#fatiando uma lista
player = ['charles', 'martina', 'michael', 'florence', 'eli']
print(player[0:3])
print(player[1:4])
print(player[:4])
print(player[2:])
print(player[-3:])

#percorrendo uma fatia com um loop
for players in player[:3]:
    print(players.title())
