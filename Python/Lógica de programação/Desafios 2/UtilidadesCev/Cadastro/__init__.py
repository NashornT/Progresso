dic = {}
pessoas= []
from time import sleep

def idade():
    try:
         idade = int(input('Idade: '))
    except:
        while True:
            print('Ocorreu um erro.')
            r = input('Idade: ')
            if r.isnumeric():
                dic['idade'] = r
                pessoas.append(dic['idade'])
                dic.clear()
                print(f'Idade Cadastrada com Sucesso.')
                break
    else:
        dic['idade'] = idade
        pessoas.append(dic['idade'])
        dic.clear()
        print(f'Idade cadastrada com Sucesso.')




def nome():
    nome = input('Nome: ')
    if nome.isnumeric() :
        while True:
            print('Ocorreu um erro.')
            r = input('Nome: ')
            if r.isalpha():
                dic['nome']=nome
                pessoas.append(dic['nome'])
                dic.clear()
                print('Nome cadastrado com sucesso.')
                break
    else:
        dic['nome'] = nome
        pessoas.append(dic['nome'])
        dic.clear()
        print('Nome cadastrado com sucesso.')

def painel():
    print('-'*30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-'*30)
    print('\033[32m1\033[m \033[33m- Ver pessoas cadastradas\033[m ')
    print('\033[32m2\033[m \033[33m- Cadastrar nova pessoa\033[m ')
    print('\033[32m3\033[m \033[33m- Sair do Sistema\033[m')
    print('-' * 30)
    opc = int(input('\033[34mSua opção:\033[m '))
    print('-' * 30)
    count = 0
    cont = 1
    if opc == 1:
        for x in pessoas:
            print(f'{"PESSOAS CADASTRADAS":^30}')
            print('-' * 30)
            print(f'{pessoas[count]}---->{pessoas[cont]} anos')
            count += 2
            cont += 2
            if count > len(pessoas) or cont > len(pessoas):
                sleep(1)
                return painel()
    if opc == 2:
        print(f'{"NOVO CADASTRO:":^30}')
        print('-' * 30)
        nome()
        idade()
        sleep(1)
        return painel()
    if opc == 3:
        print(f'{"SAINDO DO PROGRAMA":^30}')
        print('-' * 30)
        exit()

    else:
        print('\033[31mVocê Digitou uma opção invalida\033[m\n\033[33mou Não tem nenhuma pessoas cadastrada no '
              'programa ainda...\033[m')
        sleep(1)
        return painel()






painel()
