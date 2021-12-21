'''
import time
for x in range(10 , 0-1,-1):
    time.sleep(1)
    print(x)
print('FELIZ ANO NOVO!!!!!')
'''
'''
for x in range(1,50):
    if x%2==0:
        print(x)
'''
'''
y = 0
for x in range(1,500):
    if x % 3 == 0 and x * 3:
      y += x
print(y)
'''
'''
t = int(input('Digite o número que deseja mostrar a tabuada:'))
for x in range(1,11):
    print(f'{t}X{x} = {t*x} ')
'''
'''
y = 0
n = int(input('Digite um número:'))
for x in range(n,n+6):
   if x % 2 == 0:
       y += x
print(y)
'''
'''
pa1 = int(input('Digite o primeiro termo da PA.'))
pa2 = int(input('Digite a razão da PA.'))
for x in range(pa1,pa1+(10*pa2),pa2):
    print(x, end='-')
'''
'''
f = input('Digite uma palavra ou frase:').strip().upper()
g = f.split()
h = ''.join(g)
if h ==h[::-1]:
    print('Essa palavra ou frase é um palindroma.')
else:
    print('Não é um palidroma')
'''

''' print('\033[1;32m você pode entrar.\033[m ')
print('\033[1;31m você não pode entrar , tente quanto fizer 18 anos\033[m.')
'''
'''
ano,  = [],

for x in range(0,7):

    n =(int(input('Digite o ano de seu nascimento: ')))
    if (2021-n) >= 18:
      ano.append(x)
for y in ano:
    print(f'Esse são os maiores de idade: {ano.index(y)} ')
'''

'''
peso = []
for x in range(1,6):
    n =(float(input(f'Peso da {x}° pessoa: ')))
    peso.append(n)
print(f'O maior peso é  {max(peso)}KG.')
print(f'O menor peso é {min(peso)}KG.')
'''

n1 = nome , idade, sexo= [],[],[]
for x in range(4):
    n = input('Digite seu nome: ')
    i = int(input('Digite sua idade: '))
    s = input('Digite seu sexo: ')
    nome.append(n)
    idade.append(i)
    sexo.append(s)
print('-'*20)
print(nome[0],idade[0],sexo[0])
print(nome[1],idade[1],sexo[1])
print(nome[2],idade[2],sexo[2])
print(nome[3],idade[3],sexo[3])
print('-'*20)
