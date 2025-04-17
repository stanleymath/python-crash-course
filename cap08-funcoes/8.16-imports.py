''' 8.16 Imports: Usando um programa que você escreveu e que tenha apenas uma
 função, armazene essa função em um arquivo separado. Importe a função para o
 arquivo de programa principal e chame a função usando cada uma dessas abordagens:
 import nome_módulo
 from nome_módulo import nome_função
 from nome_módulo import nome_função as nf
 import nome_módulo as nm
 from nome_módulo import *'''

import formatted_name2 as nome

name = nome.get_formatted_name('stanley', 'de oliveira', 'matheus')
print(name)