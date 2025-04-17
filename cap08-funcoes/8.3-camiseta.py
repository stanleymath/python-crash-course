'''8.3 Camiseta: Crie uma função chamada make_shirt() que aceita um tamanho e o
 texto que deve ser estampado na camiseta. A função deve exibir uma frase resumindo
 o tamanho da camiseta e a mensagem estampada nela.'''

def make_shirt(tamanho, texto_estampa):
    return print(f"Tamanho da camiseta: {tamanho} \nEstampa da camiseta: {texto_estampa}")


make_shirt('M', 'Com grandes poderes vem grandes responsabilidades.')

make_shirt(tamanho='M', texto_estampa='Uma frase ai')

