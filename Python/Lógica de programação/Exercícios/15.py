'''
cont = 0
n = int(input('Digite o número que deseja mostrar a tabuada: '))
while True:
    if n < 0:
        break
    cont += 1
    print(f'{n}X{cont} = {n*cont}')
    if cont == 10 :
         e = input('Gostaria de ver outra tabuada: (S/N)').upper()
         if e == 'S':
             cont = 0
             n = int(input('Qual ??'))
         if e == 'N':
             break
'''

import random
P = input('PAR ou IMPAR ??').upper()
list = [0,1,2,3,4,5,6,7,8,9,10]
li = random.choice(list)
cont = 0

while True:
    n = int(input('Digite um número de 0 a 10. '))
    if P == 'PAR':
        if (n + li) % 2 == 0:
            li = random.choice(list)
            cont += 1
            print('Você venceu')
        else:
            break
    if P == 'IMPAR':
        if (n + li) % 3 == 0 :
            li = random.choice(list)
            cont += 1
            print('Você venceu')
        else:
            break
print(f'Você ganhou {cont} veze(s)!!')






