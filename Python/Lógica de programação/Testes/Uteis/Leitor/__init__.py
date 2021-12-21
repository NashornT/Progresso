def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('ERROR AO LER O ARQUIVO')
    else:
        print(a.read())


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
lerarquivo()





