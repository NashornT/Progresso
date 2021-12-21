from time import sleep

def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('ERROR AO LER O ARQUIVO')
    else:
        print(a.read())
def escrever(nome):
    a = open(nome,'at+')
    a.write(input(':\n'))
    a.close()



def criararq(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado  com sucesso')

def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()

    except FileNotFoundError:
        return False
    else:
        return True
def painel():
    print('-'*35)
    print('Entrando no console...')
    sleep(1)
    print('-'*35)
    p = input('Deseja guardar alguma coisa no arquivo ?? (S/N) ').strip().upper()[0]
    if p == 'S':
        escrever('teste')
    else:
        exit()
    h = input('Deseja ver o que tem escrito no arquivo ??(S/N) ').strip().upper()[0]
    if h == 'S':
        lerarquivo('teste')
    else:
        exit()


painel()