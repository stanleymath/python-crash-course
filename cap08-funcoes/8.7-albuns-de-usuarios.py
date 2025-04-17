'''8.8 Álbuns de usuários: Comece com seu programa do Exercício 8.7. Escreva um loop
 while que possibilite aos usuários inserir o artista e o título de um álbum. Após receber
 essas informações, chame make_album() com a entrada do usuário e exiba o dicionário
 criado. Não se esqueça de incluir um valor de saída no loop while'''

def make_album(artista, titulo):
    album = {
        'artista': artista,
        'titulo': titulo
    }

    return album

while True:
    print("Preencha com artista e album\n Para sair digite 'q' + enter")
    artist = input("Artista: ")
    alb = input("Album: ")

    bd = make_album(artist, alb)
    print(f"Álbuns registrados {bd}")

    if artist == 'q':
        break
    if alb == 'q':
        break

    

