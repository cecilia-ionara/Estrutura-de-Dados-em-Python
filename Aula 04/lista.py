lista1 = [12, 14, 12,-4,56, 3, 11]

lista2 = [x for x in lista1 if x%2==0]
print(lista2)

lista3 = [x**2 for x in lista1]
print(lista3)

M = lambda y: y*y
print(M(20))

print("###### Acessando normal #####")

M = [[1,2,3],[10,20,30]]
for i in M:
    print("Sublista: ", i)
    for j in i:
        print("Elemento: ",j)

print("###### Usando Range ######")
M = [[1,2,3],[10,20,30]]
for i in range(2):
    print("Sublista: ", i)
    for j in range(3):
        print("Elemento: ", j)
