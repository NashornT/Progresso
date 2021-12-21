'''
def area(a,b):
    m = a*b
    print(f'A área desejada é de {m}m²')

area(float(input('Largura:')),float(input('Comprimento')))
'''
'''
def escreva(txt):
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt))




escreva('Gustavo Barboza')
escreva('Aprendendo')
escreva('Função')
'''
'''
inicio = int(input('Inicio:'))
fim =int(input('Fim'))
passo =int(input('Passo'))

def contador(*núm):
    print('-='*30)
    print(f'contagem de {núm[0]} até o {núm[1]} de {núm[2]} em {núm[2]}')
    for x in range(núm[0],núm[1],núm[2]):
        print(f'{x} ', end='')
    print()




contador(1,10,1)
contador(10,0,-2)
contador(inicio,fim,passo)
'''
'''
from time import  sleep
def maior(* núm):
    count = maior = 0
    print('\nAnalisando valores...')
    for valor in núm:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if count == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += 1
    print(f'\nforam informados {count} valores ao todo')
    print(f'o maior foi {maior}')
maior(1,2,6,9,15)
maior(12,18,24,76)
'''
números = []
from random import  randint
def sortea(*núm):
    print('Sorteando 5 valores da lista:')
    for x in núm:
        números.append(x)
    print(números)
def SomaPar(lista):
    count = par = 0
    for x in lista:
        if x%2 == 0:
            par += x
    print(f'Somando os valores pares {par}')




sortea(randint(1,10),randint(1,20),randint(20,35),randint(40,100),randint(20,60))
SomaPar(números)