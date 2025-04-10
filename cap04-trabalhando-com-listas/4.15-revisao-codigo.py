#  4.15 Revisão do código: Escolha três dos programas que escreveu neste capítulo e
#  modifique cada um deles para atender às recomendações da PEP 8.
#  • Utilize quatro espaços para cada nível de indentação. Configure seu editor de texto
#  para inserir quatro espaços sempre que você pressionar a tecla TAB, se ainda não
#  tiver configurado (confira o Apêndice B para instruções sobre como fazer isso).
#  • Use menos de 80 caracteres em cada linha e configure seu editor para mostrar uma
#  linha-guia vertical na posição do 80º caractere.
#  • Não use excessivamente linhas em branco em seus arquivos de programa.

# 1
buffet = ('Arroz com frango', 'Lasanha', 'Feijoada', 'Galinhada', 'Purê de batat'
'a')

print("Oferecemos as seguintes refeições")
for comida in buffet:
    print(comida)

#buffet[0] = 'Salsicha'

buffet = ('Marmitex', 'Pizza', 'Feijoada', 'Galinhada', 'Purê de batata')

print("\nAtualizamos nosso cardápio")
for comida in buffet:
    print(comida)
