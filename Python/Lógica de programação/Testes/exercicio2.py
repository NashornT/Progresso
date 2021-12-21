class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def setLado(self,lado):
        self.lado = lado

    def getLado(self):
        return self.lado


p1 = Quadrado(18)


p1.setLado(20)

print(f'Lado = {p1.lado}cm')
print(f'Area = {p1.lado*p1.lado}cm²')