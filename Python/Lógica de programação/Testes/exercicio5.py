from time import sleep



class conta:
    def __init__(self,Num_conta,Nome,Saldo):
        self.Num_conta = Num_conta
        self.Nome = Nome
        self.Saldo = Saldo
    def setNome(self,Nome):
        self.Nome = Nome

    def getNome(self):
        return self.Nome

    def setSaldo(self,Saldo):
        self.Saldo = Saldo

    def getSaldo(self):
        return  self.Saldo


s = 4000
p1= conta(305.105-7,'Rodolfo',s)

print('Iniciando Banco...')
sleep(1)
print('~'*15)
while True:
    log = input('Login:')
    sen = input('Senha:')
    if log == 'gustavo' and sen == '12345':
        print('\033[32mAcesso Liberado\033[m')
        sleep(1)
        break
    else:
        print('\033[31mAcesso Negado\033[m')
        print('login ou Senha Invalidos')
print('Acessando conta corrente...')
sleep(0.4)
while True:
    print('~'*15)
    print(f'Nome:{p1.Nome}\nSaldo:{p1.Saldo}')
    print('~'*15)
    p = int(input('1.altera nome\n2.Sacar\n3.Depositar\n4.Sair\n'))
    if p == 1 :
        Mn = input('Novo Nome:')
        p1.setNome(Mn)
        sleep(0.3)
        print('\033[32mNome Alterado com Sucesso\033[m')
        sleep(1)
    elif p == 3:
        try:
            Depo = int(input('Valor a ser Depositado:'))
        except:
            print('\033[31mOcorreu um erro , ao digitar os valores.\033[m ')
            sleep(0.3)
        else:
            print(f'\033[32mValor depositado com sucesso\033[m')
            p1.setSaldo(p1.Saldo+Depo)
            sleep(1)
    elif p == 4 :
        print('Obrigado e volte sempre.')
        sleep(0.4)
        break
    elif p == 2:
        try:
            Saque = int(input('Valor a ser Sacado:'))
            if Saque > p1.Saldo:
                print('\033[31mValor indisponivel na conta\033[m')
                sleep(1)
            else:
                print(f'\033[32mValor sacado com sucesso\033[m')
                p1.setSaldo(p1.Saldo - Saque)
                sleep(1)
        except:
            print('\033[31mOcorreu um erro , ao digitar os valores.\033[m ')
            sleep(0.3)




