'''8.11 Mensagens arquivadas: Comece sua tarefa a partir do Exercício 8.10. Chame a
 função send_messages() com uma cópia da lista de mensagens. Após chamar a
 função, exiba ambas as listas para mostrar que a lista original reteve suas mensagens.'''
        
def send_messages(mensagens2):
    while mensagens2:
        messages = mensagens2.pop()
        print(messages)
        sent_messages.append(messages)
        print(f"{sent_messages}")
    


msgs = ['Um dia após o outro', 'Técnicas de aperfeiçoamento pessoal', 'Utilizando pomodoro no dia a dia']
sent_messages = []

print(send_messages(msgs[:]))
print(msgs)

