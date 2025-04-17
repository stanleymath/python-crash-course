''' 8.9 Mensagens: Crie uma lista com uma série de mensagens curtas de texto. Passe a
 lista para uma função chamada show_messages(), que exiba cada mensagem de texto.'''

def show_messages(mensagens):
    for mensagem in mensagens:
        print(f"{mensagem}")
        


msgs = ['Um dia após o outro', 'Técnicas de aperfeiçoamento pessoal', 'Utilizando pomodoro no dia a dia']

print(show_messages(msgs))

