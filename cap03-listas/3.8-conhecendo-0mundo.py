#lista original
lugares = ['Maringá', 'São Paulo', 'Alaska', 'Rússia']
print(lugares)

#organizando lista de maneira temporária
print(sorted(lugares))
#lista original
print(lugares)

#lista ordenada de maneira reverse de modo permanente
lugares.reverse()
print(lugares)

#aplicando o reverse no reverse para inverter a lista anterior
lugares.reverse()
print(lugares)

lugares.sort(reverse=True)
print(lugares)