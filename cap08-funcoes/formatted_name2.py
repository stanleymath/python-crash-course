# definindo um valor opcional

def get_formatted_name(first_name, last_name, midle_name=''):
    '''Retorna um nome completo, elegantemente formatado'''
    if midle_name:
        full_name = f"{first_name} {midle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musican = get_formatted_name('jimi', 'hooker', 'lee')
# print(musican)