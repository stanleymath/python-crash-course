'''8.14 Carros: Crie uma função que armazena informações sobre um carro em um
 dicionário. A função deve sempre receber um fabricante e um nome de modelo. Em
 seguida, deve aceitar um número arbitrário de argumentos nomeados. Chame a função
 com as informações necessárias e dois outros pares nome-valor, como uma cor ou um
 recurso opcional. Sua função deve funcionar mais ou menos assim:
 car = make_car('subaru', 'outback', color='blue', tow_package=True)
 Exiba o dicionário retornado para garantir que todas as informações foram
 corretamente armazenadas.'''

def info_carro(fabricante, modelo, **args):
    args['fabricante'] = fabricante
    args['modelo'] = modelo
    print(args)


carro = info_carro('BMW', 'lm4', cor = 'preto', travas_eletricas = True)