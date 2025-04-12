sandwich_orders = ['parrudão', 'xtudo', 'xsheedar', 'xsalada', 'pastrami', 
                   'xbacon', 'simples', 'pastrami', 'pastrami']

n = 0
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    for i in sandwich_orders:
        finalizados = sandwich_orders.pop()
        print(finalizados)
        
