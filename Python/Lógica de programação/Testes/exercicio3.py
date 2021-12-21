from time import sleep

print('Iniciando programa...')
sleep(1)
while True:
    try:
        r1 = float(input('Digite o valor da altura do comodo.'))
        break
    except:
        print('valor digitado invalido, tente de novo .')
while True:
    try:
        r2 = float(input('Digite o valor da base do comodo. '))
        break
    except:
        print('valor digitado invalido , tente de novo .')
print('Calculando...')
sleep(1)

class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura  = altura

    def setBase(self,base):
        self.base = base

    def getBase(self):
        return self.base

    def setAltura(self,altura):
        self.altura = altura

    def getAltura(self):
        return self.altura



p1 = Retangulo(20,18)
p1.setBase(r2)
p1.setAltura(r1)

print('Área de um piso = 1m²')
print('Comprimento de um rodapé = 1m')

print(f' Base={p1.base}m,Altura={p1.altura}m')
sleep(0.3)
print(f'Área={p1.base * p1.altura}m²')
sleep(0.3)
print(f'Perimetro={(2 * p1.altura) + (2 * p1.base)}m')
sleep(0.3)
print(f'Quantidade de pisos necessaria = {(r2*r1)/1}')
sleep(0.3)
print(f'Quantidade de rodapés = {r2/1} ')






