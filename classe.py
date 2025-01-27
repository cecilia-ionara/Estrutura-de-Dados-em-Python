class fila:
    def __init__(self):
        self.item=[]
    def adicionar(self,i):
        self.item.append(i)
    def remover(self):
        self.item.pop(0)
    def mostrar(self):
       return self.item

    f1=fila()
    for i in range(3):
        f1.adicionar(int(input("Valor: ")))
    print(f1.mostrar())
    f1.remover()
    print(f1.mostar())