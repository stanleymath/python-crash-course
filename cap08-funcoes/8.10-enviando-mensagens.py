''' 8.10 Enviando mensagens: Comece com uma cópia do seu programa do Exercício 8.9.
 Escreva uma função chamada send_messages() para exibir cada mensagem de texto e
 passe cada mensagem para uma nova lista chamada sent_messages à medida que é
 exibida. Após chamar a função, exiba ambas as listas para ter certeza de que as
 mensagens foram corretamente transferidas.
'''
        
def send_messages(mensagens2):
    while mensagens2:
        messages = mensagens2.pop()
        print(messages)
        sent_messages.append(messages)
        print(f"{sent_messages}")
    


msgs = ['Um dia após o outro', 'Técnicas de aperfeiçoamento pessoal', 'Utilizando pomodoro no dia a dia']
sent_messages = []

print(send_messages(msgs))

