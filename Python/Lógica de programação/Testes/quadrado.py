from time import sleep
def painel():
    print('-='*15)
    print(f'{"Bem-Vindo":^30}')
    print('-='*15)
    sleep(1)
    p = input('Deseja entrar no console ? (S/N)').strip().upper()[0]
    if p == 'S':
        print('Entrando...')
        sleep(1)
        estudo()
    elif p == 'N':
        sleep(1)
        print('\033[31mVAI TOMAR NO CU ENTÃO\033[m')
        exit()


def estudo():
     op = int(input('Escolha uma opção : (1/2)'))
     if op == 1:
        sleep(1)
        print('Gustavo é pica')
     elif op == 2:
        sleep(1)
        print('Gustavo é um mané')
     else:
        print('\033[31mOpção invalida\033[m ')
painel()
