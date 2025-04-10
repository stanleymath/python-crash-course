# 3.10 Funções: Pense em coisas que você conseguiria armazenar em uma lista. Por
#  exemplo, você pode criar uma lista de montanhas, rios, países, cidades, idiomas, ou
#  qualquer outra coisa que quiser. Crie um programa com uma lista contendo esses itens
#  e, em seguida, use cada função apresentada neste capítulo, pelo menos, uma vez.

# 1 Cria uma lista
listaAleatoria = ['inglês', 'Everest', 'Holanda', 'Marte', 'Júpiter', 'Plutão', 'SpaceX', 'Naruto']

# 2 Mostra a lista
print(listaAleatoria)

# 3 Mostra um índice de escolha na lista
print(f"{listaAleatoria[2]} ou {listaAleatoria[5]}")

# 4 del deleta um item de escolha na lista de modo permanente
del listaAleatoria[0]
print(f"Inglês que era o índice 0 foi deletado da lista: {listaAleatoria}")

# 5 append() adiciona um índice ao fim da lista
listaAleatoria.append('Honda')
print(f"Foi adicionado Honda ao fim da lista utilizando o método append() {listaAleatoria}")

# 6 insert() adiciona um índice na lista em uma posição desejada (não deleta o índice da mesma posição, apenas movimenta)
listaAleatoria.insert(0, 'Francês')
print(f"Francês foi adicionado a lista utilizando o método insert() na posição 0: {listaAleatoria}")

# 7 aplicando sort() para ordenar de maneira alfabética permanente
listaAleatoria.sort()
print(f"Lista ordenada de maneira permanente utilizando sort(): {listaAleatoria}")

# 8 aplicando sorte() de maneira reversa para inverter a lista ordenada de modo permanente
listaAleatoria.sort(reverse=True)
print(f"Lista de maneira reversa com sort(): {listaAleatoria}")

# 9 aplicando apenas o reverse para inverter a lista
listaAleatoria.reverse
print(f"Lista invertida com reverse:   {listaAleatoria}")

# 10 deletando um índice de e guardando em uma variável para usar novamente
empresa = listaAleatoria.pop(0)
print(f"O índice excluído foi guardado em {empresa} e já não consta mais na lista {listaAleatoria}")

# 11 Organiza em ordem alfabética mas não permanente
print(sorted(listaAleatoria))

