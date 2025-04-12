favorite_places = {
    'stanley': ['maringá', 'caldas-novas', 'ouvidor'],
    'samanta': ['são paulo', 'fortaleza'],
    'luh': ['foz do iguaçu', 'paraguai', 'morrinhos']
    }

for nome, lugares in favorite_places.items():
    print(f"\nPessoa: {nome}:: Lugares favoritos são: ")

    for lugar in lugares:
        print(lugar)