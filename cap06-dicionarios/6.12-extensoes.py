#  6.12 Extensões: Agora que já estamos trabalhando com exemplos complexos o
#  suficiente para que sejam mais desenvolvidos de diferentes maneira, use um dos
#  programas de exemplo deste capítulo e o amplie, adicionando chaves e valores novos,
#  alterando o contexto do programa ou melhorando a formatação da saída.

# criando 150 aliens 
# 50 verdes
# 50 amarelos
# 50 vermelhos

#lista que guardará todos os aliens
aliens = []

#cria 150 aliens
for qtd in range(1,151):
    novo_alien = {
          'color': 'verde'
           }
    aliens.append(novo_alien)

for alien in aliens[:49]:
    if alien['color'] == 'verde':
        alien['color'] = 'amarelo'

for alien in aliens[50:100]:
    if alien['color'] == 'verde':
        alien['color'] = 'vermelho'

print(aliens[:49])
print(aliens[50:100])
print(aliens[101:])