# importa o modulo inteiro
#import pizza2
# importa somente funcções específicas
#from pizza2 import make_pizza
# importa à função como mp() (alias)
#from pizza2 import make_pizza as mp
# usando as para atribuir um lias a um módulo
import pizza2 as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

