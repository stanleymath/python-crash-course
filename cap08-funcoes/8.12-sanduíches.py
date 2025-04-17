''' 8.12 Sanduíches: Crie uma função que aceite uma lista de itens que uma pessoa quer
 em um sanduíche. A função deve ter um parâmetro que colete todos os itens
 fornecidos na chamada de função e deve exibir um resumo do sanduíche que está
 sendo solicitado. Chame a função três vezes, com um número diferente de argumentos
 a cada vez.'''

def fazer_sanduiche(*itens):
    print("\nSanduíche com os seguintes indredientes")
    for item in itens:
        print(f" - {item}")
    print("Sanduíche pronto")


fazer_sanduiche('pão', 'carne', 'ovo')
fazer_sanduiche('pão', 'carne', 'ovo', 'alface')
fazer_sanduiche('pão', 'queijo')
