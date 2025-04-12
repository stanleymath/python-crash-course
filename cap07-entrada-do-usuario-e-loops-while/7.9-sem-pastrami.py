# 7.9 Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, assegure-se de que
#  o sanduíche 'pastrami' apareça na lista pelo menos três vezes. Faça mais um código
#  perto do início de seu programa, exibindo uma mensagem que informe que a
#  lanchonete está sem pastrami e, em seguida, use um loop while para remover todas as
#  ocorrências de 'pastrami' em sandwich_orders. Faça questão de que nenhum sanduíche
#  de pastrami acabe em finished_sandwiches..

print("A lanchonete está sem pastrami")
sandwich_orders = ['parrudão', 'xtudo', 'xsheedar', 'xsalada', 'pastrami', 
                   'xbacon', 'simples', 'pastrami', 'pastrami']

finished_sandwiches = []



while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    for _ in sandwich_orders:
        sandwich_orders.reverse()
        finalizados = sandwich_orders.pop()
        finished_sandwiches.append(finalizados)
        print(f"Seu lanche {finalizados} está pronto")

n = 0

print(f"\nOs seguintes lanches estão preparados!!")
for lanche in finished_sandwiches:
    n += 1
    print(f"{n}: {lanche}")





