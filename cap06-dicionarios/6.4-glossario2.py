#  6.4 Glossário 2: Agora você sabe como percorrer um dicionário com um loop, limpe o
#  código do Exercício 6.3 (página 
# 138) substituindo sua série de print() por um loop que
#  percorre as chaves e os valores do dicionário. Quando tiver certeza de que seu loop
#  funciona, adicione mais cinco termos Python ao seu glossário. Quando executar seu
#  programa novamente, essas palavras e dignificados novos devem ser incluídos
#  automaticamente na saída.

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
    'continue':
    'Prossegue pulando o valor selecionado',
    'Break':
    'Para o código',
    'if':
    'Condição se',
    'elif':
    'Condição se não se',
    'else':
    'Condição se não',
    }

for k,v in glossario_python.items():
    print(f"{k}: {v}")