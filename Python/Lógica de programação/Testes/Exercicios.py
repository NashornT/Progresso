class Bola:
    def __init__(self, cor, raio, material):
        self.cor = cor
        self.raio = raio
        self.material = material

    def setCor(self,cor):
        self.cor = cor

    def getCor(self):
        return self.cor

p1 = Bola('Azul','5cm','Ferro')
p2 = Bola('Vermelha','7cm','Madeira')


p1.setCor('verde')
p2.setCor('preto')
print(p1.cor)
print(p2.cor)
