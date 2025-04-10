dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#tentando alterar elemento da tupla
#dimensions[0] = 250
# retorna o erro TypeError: 'tuple' object does not support item assignment

# o elemento da tupla é definido pela , a direita o elemento como por exemplo:
my_t = (3,)

#Tuplas com um único elemento não são muito comuns

#percorrendo elementos em uma tupla
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#sobrescrevendo uma tupla
dimensions = (200, 50)
print("\nOriginal dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    