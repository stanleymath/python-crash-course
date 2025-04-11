#  5.2 Mais testes condicionais: não é necessário restringir o número de testes a 10. Caso
#  queira executar mais comparações, escreva mais testes e os adicione a
#  conditional_tests.py. Gere, pelo menos, um resultado True e um False para cada
#  condição a seguir:
#  • Testes com operadores de igualdade e de diferença com strings.
#  • Testes usando o método lower().
#  • Testes numéricos com operadores de igualdade e de diferença, maior e menor que,
#  maior ou igual que e menor ou igual a.
#  • Testes com as palavras reservadas and e or.
#  • Testes para averiguar se um valor consta em uma lista.
#  • Testes para averiguar se um valor não consta em uma lista.

personagem = 'Naruto uzumaki'
print(personagem == 'Naruto uzumaki')

cidade = 'Rio de janeiro'
print(cidade.lower() == 'rio de janeiro')

n = 19
print(n == 15)
print(n != 19)
print(n > 20)
print(n < 21)
print(n <= 21)
print(n >= 21)