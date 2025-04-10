# # 4.5 Somando um milhão: crie uma lista com números de um a um milhão e, em
#  seguida, use min() e max() a fim de garantir que sua lista realmente comece em um e
#  termine em um milhão. Além disso, use a função sum() para ver a rapidez com que o
#  Python pode efetuar a soma de um milhão de números.

lista = list(range(1,1000001))

print(min(lista))
print(max(lista))
print(sum(lista))
