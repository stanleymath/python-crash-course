#  7.3 Múltiplos de dez: Solicite ao usuário um número e informe se o número é múltiplo
#  de 10 ou não

num = int(input("Digite um número: "))

if num % 10 == 0:
    print(f"{num} é múltiplo de dez")
else:
    print(f"{num} não é múltiplo de dez")