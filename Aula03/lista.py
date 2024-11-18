import random

valores = [-20, 23, -2, 30, 32]

#embaralhar
random.shuffle(valores)
print(valores)
#vai de um a 5 com steps de dois em dois
#lista1 = valores[1:4:2]

lista1 = valores[:]
print(lista1)
print(valores)
print(id(valores))
print(id(lista1))

