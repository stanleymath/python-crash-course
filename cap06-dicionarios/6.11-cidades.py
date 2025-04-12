cities = {
    'maringá': {
        'país': 'brasil',
        'população': '800 mil habitantes',
        'fato': 'bonita demais',
        },
    'são paulo': {
        'pais': 'brasil',
        'população': '12.000.000 milhões de habitantes',
        'fato': 'poluída',
        },
    'foz do iguaçu':{
        'país': 'brasil',
        'população': '200 mil habitantes',
        'fato': 'exótica',
        },

        }

for cidades, infos in cities.items():
    print(f"\nCidade: {cidades} e algumas informações: ")

    for info, values in infos.items():
        print(f"{info}: {values}")



