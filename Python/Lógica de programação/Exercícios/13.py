'''
x = 'M'
es = input('Selecione seu sexo(M/F): ').upper()
while ( x != es ):
    if es == 'F':
        break
    print('\033[31m Opção invalida! tente denovo\033[m !!')
    es = input('Selecione seu sexo(M/F): ').upper()

print('\033[32m Dado recebido , Obrigado pela participação\033[m ')
'''
'''
import random
li = int(input('Adivinnhe o número que estou pensando de (0,10):'))
list = [0,1,2,3,4,5,6,7,8,9,10]
p = random.choice(list)

count = 0
while li != p:
    if li != p :
        print('\033[31m Uma pena  você falhou ,tente de novo \033[m!!!')
        li = int(input('Adivinnhe o número que estou pensando de (0,10):'))
        count += 1
    elif li == p :
        break

print(f'\033[32m Parabéns ,você acertou!!! , foram {count} tentativas.')
'''
'''
e = input('Deseja entrar no projeto calculadora ?? (\033[32mS\033[m/\033[31mN\033[m): ').upper()
while e == 'S':
    n1 = float(input('Digite o primeiro número que deseja fazer a operação:'))
    n2 = float(input('Digite o segundo número que deseja fazer a operação:'))
    op = int(input('Selecione uma opção \n'
                   '\033[33m(1)\033[m\033[34mSOMAR\033[m '
                   '\n\033[33m(2)\033[m\033[34mMULTIPLICAR\033[m '
                   '\n\033[33m(3)\033[m\033[34mMAIOR\033[m '
                   '\n\033[33m(4)\033[m\033[34mNOVOS NÚMEROS\033[m'
                   '\n\033[33m(5)\033[m\033[34mDIVISÃO\033[m'
                   '\n\033[33m(6)\033[m\033[34mEXPONENCIAÇÃO\033[m'
                   '\n\033[33m(7)\033[m\033[34mSAIR DO PROGRAMA\033[m '
                   '\n : '))
    if op == 1:
        print(n1+n2)
        e = input('Deseja continuar(\033[32mS\033[m/\033[31mN\033[m)').upper()
    if op == 2 :
        print(n1*n2)
        e = input('Deseja continuar(\033[32mS\033[m/\033[31mN\033[m)').upper()
    if op == 3 :
        if n2 > n1 :
            print(f'O maior número é {n2}')
            e = input('Deseja continuar(\033[32mS\033[m/\033[31mN\033[m)').upper()
        elif n1 > n1 :
            print(f'O maior número é {n1}')
            e = input('Deseja continuar(\033[32mS\033[m/\033[31mN\033[m)').upper()
    if op == 4 :
        print()
    if op == 5:
        h1 = int(input('Gostaria de dividir:'
                   '\n1. o primerio pelo segundo'
                   '\n2. o segundo pelo primeiro \n: '))
        if h1 == 1:
            print(n1/n2)
            e = input('Deseja continuar(\033[32mS\033[m/\033[31mN\033[m)').upper()
        elif h1 == 2:
            print(n2/n1)
            e = input('Deseja continuar(\033[32mS\033[m/\033[31mN\033[m)').upper()
    if op == 6:
        h2 = int(input('Gostaria de elevar:'
                       '\n1. o primeiro elevado ao segundo'
                       '\n2. o segundo elevado ao primeiro '
                       '\n: '))
        if h2 == 1:
            print(n1**n2)
            e = input('Deseja continuar(\033[32mS\033[m/\033[31mN\033[m)').upper()
        if h2 == 2:
            print(n2**n1)
            e = input('Deseja continuar(\033[32mS\033[m/\033[31mN\033[m)').upper()
    if op == 7:
        break

print('Saindo do programa...')
'''
from math import prod
n = int(input('Digite um  número inteiro que gostaria de ver o fatorial. '))
li=[]
count = 0
while (n - count) != 0 :
    if count == 0:
        print(n, end='--')
    if n != 0:
        count += 1
        print(  f'{n-count}' , end='--')
        li.append(n-count)
        if (n-count) == 1:
            break
if n == 0:
    print(1)
print(':',f'{prod(li)*n}'  )
