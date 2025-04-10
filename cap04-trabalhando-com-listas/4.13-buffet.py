#  4.13 Buffet: Um restaurante com serviço de buffet oferece somente cinco refeições
#  básicas. Pense em cinco refeições simples e armazene-as em uma tupla.
#  • Use um loop for para exibir cada refeição que o restaurante oferece.
#  • Tente modificar um dos elementos e verifique se o Python rejeita a mudança.
#  • O restaurante muda seu cardápio, substituindo dois dos elementos por refeições
#  diferentes. Adicione uma linha que reescreva a tupla e, depois, use um loop for para
# exibir cada um dos elementos no menu reformulado.

buffet = ('Arroz com frango', 'Lasanha', 'Feijoada', 'Galinhada', 'Purê de batata')

print("Oferecemos as seguintes refeições")
for comida in buffet:
    print(comida)

#buffet[0] = 'Salsicha'

buffet = ('Marmitex', 'Pizza', 'Feijoada', 'Galinhada', 'Purê de batata')

print("\nAtualizamos nosso cardápio")
for comida in buffet:
    print(comida)
