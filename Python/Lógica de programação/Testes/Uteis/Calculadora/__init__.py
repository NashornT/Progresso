from time import  sleep
from math import prod
def painel():
    print('-'*35)
    print(f'\033[34mPROJETO CALCULADORA\033[m')
    print(f'\033[34mCARREGANDO...\033[m')
    sleep(1)
    menu()


def menu():
    print('-'*35)
    print('\033[32m1\033[m - \033[36mSOMAR\033[m\n\033[32m2\033[m - \033[36mSUBTRAIR\033[m\n\033[32m3\033[m - '
          '\033[36mMULTIPLICAR\033[m\n\033[32m4\033[m'
          ' - \033[36mDIVIDIR\033[m\n\033[32m'
          '5\033[m - \033[36mPOTENCIAÇÃO\033[m\n\033[32m6\033[m - \033[36mFATORIAL\033[m'
          '\n\033[32m7\033[m - \033[36mSAIR\033[m ')
    print('-' * 35)
    try:
        r = int(input('\033[32mEscolha sua opção:\033[m'))
        sleep(0.3)
    except :
        print('\033[31mOPÇÃO INVALIDA , redirecionando para o menu...\033[m')
        sleep(1)
        return menu()
    else:
        if r == 1:
            li = []
            n1 = 1
            while True:
                s = int(input(f'\033[32mDigite o {n1}° número\033[m '))
                li.append(s)
                n1 += 1
                if n1 >= 3:
                    p = input('\033[32mDeseja Somar:\033[m (\033[32mS\033[m/\033[31mN\033[m)').strip().upper()[0]
                    if p == 'S':
                        print(f'\033[33mA soma de todos os {len(li)}  números digitados foi:\033[m \033[35m{sum(li)}'
                              f'\033[m')
                        print(f'\033[33mRedirecionando ao menu principal...\033[m')
                        sleep(1)
                        return menu()

        if r == 2:
            n2 = 1
            s1 = int(input(f'\033[32mDigite o {n2}° número\033[m'))
            n2 += 1
            s2 = int(input(f'\033[32mDigite o {n2}° número\033[m'))
            print(f'\033[33mA subtração dos 2 números deu:\033[m \033[35m{s1 - s2}\033[m')
            print(f'\033[33mRedirecionando ao menu principal...\033[m')
            sleep(1)
            return menu()
        if r == 3:
            n3 = 1
            s1 = int(input(f'\033[32mDigite o {n3}° número\033[m'))
            n3 += 1
            s2 = int(input(f'\033[32mDigite o {n3}° número\033[m'))
            print(f'\033[33mA multiplicação dos 2 números deu:\033[m \033[35m{s1*s2}\033[m')
            print(f'\033[33mRedirecionando ao menu principal...\033[m')
            sleep(1)
            return menu()
        if r == 4 :
            s1 = int(input(f'\033[32mDigite o dividendo:\033[m'))
            s2 = int(input(f'\033[32mDigite o divisor:\033[m '))
            print(f'\033[33mA divisão dos 2 números deu:\033[33m \033[35m{s1/s2}\033[m')
            r = input('\033[33mGostaria de saber o resto ?\033[m (\033[32mS\033[m/\033[31mN\033[m)').strip().upper()[0]
            if r == 'S':
                print(f'\033[33mO resto da divisão deu:\033[m \033[35m{s1%s2}\033[m')
            print(f'\033[33mRedirecionando ao menu principal...\033[m')
            sleep(1)
            return menu()
        if r == 5:
            s1 =  int(input(f'\033[32mDigite a base\033[m'))
            s2 = int(input(f'\033[32mDigite o expoente\033[m'))
            print(f'\033[33mA exponenciação da base {s1} no expoente {s2} foi:\033[m \033[35m{s1**s2}\033[m')
            print(f'\033[33mRedirecionando ao menu principal...\033[m')
            sleep(1)
            return menu()
        if r == 6 :
            li = []
            s1 = int(input(f'\033[32mDigite o número que deseja ver o fatorial.\033[m'))
            print(f'\033[36mCalculando fatorial...\033[m')
            sleep(1)
            for x in range(s1,0,-1):
                li.append(x)
                print(f'{x}', end='-')
            print(f'>{prod(li)}')
            return menu()
        if r == 7:
            print('\033[33mFECHANDO PROGRAMA...\033[m')
            sleep(1)
            exit()
        else:
            print('\033[31mOPÇÃO INVALIDA , redirecionando para o menu...\033[m')
            sleep(1)
            return menu()




painel()