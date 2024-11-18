valores = ["Olá", 23, -2, [1, 2, 3]]
valores[2] = [1, 2,3,4]

for i in valores:
    print("Elemento",i)
for i in range(len(valores)):
    print("Posição: ",i)
for i in enumerate(valores):
    print(i)