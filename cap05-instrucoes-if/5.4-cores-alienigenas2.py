#  5.4 Cores de alienígenas #2: Escolha uma cor para um alienígena, como no
#  Exercício 5.3, e escreva uma sequência if-else.
#  • Se a cor do alienígena for verde, exiba uma afirmação de que o jogador acabou de
#  ganhar 5 pontos por abrir fogo contra um alienígena.
#  • Se a cor do alienígena não for verde, exiba uma afirmação de que o jogador acabou
#  de ganhar 10 pontos.
#  • Escreva uma versão desse programa que execute o bloco if e outra que execute o
#  bloco else.

# versao if
alien_color = 'green'

if alien_color == 'green':
    print("Você ganho 5 pontos")
else:
    print("Você ganhou 10 pontos")


# versao else
alien_color = 'black'

if alien_color == 'green':
    print("Você ganhou 5 pontos")
else:
    print("Você ganhou 10 pontos")