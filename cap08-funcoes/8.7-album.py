'''8.7 Álbum: Escreva uma função chamada make_album() que crie um dicionário
 representando um álbum de música. A função deve ter o nome de um artista e o título
 de álbum, e deve retornar um dicionário com essas duas informações. Utilize a função
 para criar três dicionários representando álbuns distintos. Exiba cada valor de retorno
 para mostrar que os dicionários estão armazenando adequadamente as informações do
 álbum.'''

def make_album(artista, titulo):
    album = {
        'artista': artista,
        'titulo': titulo
    }

    return album

album1 = make_album('Legião urbana', 'xxxx')
album2 = make_album('AC/DC', 'yyyyyy')
album3 = make_album('Avenged Sevenfold', 'zzzzz')

print(album1)
print(album2)
print(album3)