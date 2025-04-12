# 7.8 Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com o nome de
#  diversos sanduíches. Depois, crie uma lista vazia chamada finished_sandwiches.
#  Percorra a lista de pedidos de sanduíches com um loop e exiba uma mensagem para
#  cada pedido, como: Seu lanche de atum está pronto. Conforme cada sanduíche é
#  preparado, passe-os para a lista de sanduíches prontos. Após todos os sa.nduíches
#  terem sido preparados, exiba uma mensagem enumerando cada um deles.

sandwich_orders = ['parrudão', 'xtudo', 'xsheedar', 'xsalada', 'xbacon', 'simples']
finished_sandwiches = []

while sandwich_orders:
    for n in sandwich_orders:
        sandwich_orders.reverse()
        finalizados = sandwich_orders.pop()
        finished_sandwiches.append(finalizados)
        print(f"Seu lanche {finalizados} está pronto")

n = 0

print(f"Os seguintes lanches foram preparados!")
for lanches in finished_sandwiches:
    n += 1
    print(f"\n{n}:{lanches}")





