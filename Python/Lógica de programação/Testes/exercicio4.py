from time import sleep
print('Abrindo rede de dados...')
sleep(1)
print('Inicalizando...')
r1 = input('Nome:')
while True:
    try:
        r2 = float(input('Idade:'))
        break
    except:
        print('\033[31mVocê Digitou um valor invalido.\033[m')
while True:
    try:
        r3 = float(input('Peso:'))
        break
    except:
        print('\033[31mVocê Digitou um valor invalido.\033[m')
while True:
    try:
        r4 = float(input('Altura:'))
        break
    except:
        print('\033[31mVocê Digitou um valor invalido.\033[m')


class pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso= peso
        self.altura = altura


    def setIdade(self, idade):
        self.idade = idade


    def getIdade(self):
        return  self.idade

    def setPeso(self,peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def setCrescer(self,altura):
        self.altura = altura

    def getCrescer(self):
        return self.altura


p1 = pessoa(r1,r2,r3,r4)
print('~'*15)
print(f'Nome:{p1.nome}\nAltura:{p1.altura}'
      f'\nPeso:{p1.peso}\nIdade:{p1.idade}')
print('~'*15)
while True:
    op = input('Deseja mudar alguma caracteristica: (S/N)').strip().upper()[0]
    if op == 'S':
        op1 = int(input('1.Idade\n2.Peso\n3.Altura\n4.Sair'))
        if op1 == 1:
            id = float(input('Idade:'))
            p1.setIdade(id)
            if id > r2:
                print('\033[33mEnvelhecendo...\033[m')
                sleep(1)
            elif id < r2:
                print('\033[32mRejuvenecendo...\033[m')
                sleep(1)
            print('Alterando Pessoa...')
            sleep(1)
            print('~' * 15)
            print(f'Nome:{p1.nome}\nAltura:{p1.altura}'
                  f'\nPeso:{p1.peso}\nIdade:{p1.idade}')
            print('~' * 15)
        elif op1 == 2:
            id1 = float(input('Peso:'))
            p1.setPeso(id1)
            if id1 > r3:
                print('\033[33mEngordando...\033[m')
                sleep(1)
            elif id1 < r3:
                print('\033[32mEmagrecendo...\033[m')
                sleep(1)
            print('Alterando Pessoa...')
            sleep(1)
            print('~' * 15)
            print(f'Nome:{p1.nome}\nAltura:{p1.altura}'
                  f'\nPeso:{p1.peso}\nIdade:{p1.idade}')
            print('~' * 15)
        elif op1 == 3:
            id2 = float(input('Altura:'))
            p1.setCrescer(id2)
            if id2 > r4:
                print('\033[32mCrescendo...\033[m')
                sleep(1)
            elif id2 < r4:
                print('\033[33mEnconhendo...\033[m')
                sleep(1)
            print('Alterando Pessoa...')
            sleep(1)
            print('~' * 15)
            print(f'Nome:{p1.nome}\nAltura:{p1.altura}'
                  f'\nPeso:{p1.peso}\nIdade:{p1.idade}')
            print('~' * 15)
        elif op1 == 4:
            print('Criando Pessoa...')
            sleep(1)
            print('~' * 15)
            print(f'Nome:{p1.nome}\nAltura:{p1.altura}'
                  f'\nPeso:{p1.peso}\nIdade:{p1.idade}')
            print('~' * 15)
            break
    if op == 'N':
        break


