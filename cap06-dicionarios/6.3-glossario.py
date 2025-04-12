#  6.3 Glossário: Um dicionário Python pode ser usado para modelar um dicionário real.
#  Contudo, para evitar confusão, vamos chamá-lo de glossário.
#  • Pense em cinco palavras do mundo de programação que você aprendeu nos
#  capítulos anteriores. Use essas palavras como chaves em seu glossário e armazene
#  seus significados como valores.
#  • Exiba cada palavra e seu significado como uma saída elegantemente formatada. É
#  possível até mesmo exibir a palavra seguida por dois-pontos e depois seu significado
#  ou a palavra em uma linha e, em seguida, exibir seu significado indentado em uma
#  segunda linha. Use o caractere quebra de linha (\n) para inserir uma linha em branco
#  entre cada par palavra-significado em sua saída.

glossario_python = {
    'def':
    'Define uma função',
    'print':
    'Mostra na tela',
    'in':
    'Dentro',
    'for':
    'Loop a',
    'while':
    'Loop b',
    }

for palavra in glossario_python:
    print(f"\n{palavra}:{glossario_python[palavra]}")