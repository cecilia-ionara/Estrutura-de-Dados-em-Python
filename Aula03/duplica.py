valores = [2, 23, 544, 342, 23]
def duplica(lista):
    posicao = 0
    for i in lista:
        lista[posicao] = i * 2
        posicao += 1
    return lista

print(duplica([-2, "OI", 100]))