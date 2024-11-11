#pilha, encadeamentos
def calcularNumeros(x, y, z):
    m = x+y
    n = z*Multiplica(x,y)
    r = m + n
    return (r)

def Multiplica(a, b):
    r = a * b
    return r

print(calcularNumeros(3, 4, 5))

