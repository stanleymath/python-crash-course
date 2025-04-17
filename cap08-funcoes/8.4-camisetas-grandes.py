'''8.4 Camisetas grandes: Modifique a função make_shirt() para que as camisetas sejam
 grandes por padrão com a seguinte frase estampada: Eu amo Python. Escreva uma
 camiseta grande e uma média com a mensagem padrão e uma camiseta de qualquer
 tamanho com uma frase diferente.'''

def make_shirt(texto_estampa='Eu amo python', tamanho='G'):
    return print(f"Tamanho: {tamanho} \nEstampa da camiseta: {texto_estampa}")


make_shirt()
make_shirt(tamanho='M')