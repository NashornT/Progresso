'''
num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze'
       ,'quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
dig = int(input('Digite um número de 0 a 20: '))
while dig < 0 or dig > 20 :
    print('\033[31mERROR, número invalido\033[m')
    dig = int(input('Digite um número de 0 a 20 '))
print(f'O número digitado foi {num[dig]}')
'''
'''
times = ('Atletico-Mg','Palmeiras','Flamengo','Bragantino' ,'Fortaleza'
         ,'Corinthians','Internacional','Fluminese','Cuiabá','América-MG',
         'Atlético-GO','São Paulo','Ceará SC','Athletico-PR','Santos',
         'Bahia','Sport Recife','Juventude','Grêmio','Chapecoense')
cont = 0
count = 0
print('-'*35)
print('Os cincos primeiros times foram')
for x in range(1,len(times)):
    print(f'o {x}° foi o {times[count]} ')
    count += 1
    cont += 1
    if cont == 5:
        break
print('-'*35)
pass
con = 20
conti = 19
print('-'*35)
print('Os quatro ultimos colocados foram')
for y in range(20,0,-1):
    print(f'o {y}° foi o {times[conti]} ')
    conti -=1
    con -= 1
    if con == 16:
        break
print('-'*35)
pass
print('-'*35)
print('A ordem Alfabetica dos times é... ')
print(f'{sorted(times)}')
print('-'*35)
'''
'''
y = []
import random
for c in range(0,5):
    x = (random.random())
    y.append(x)
print(y)
print(f'o maior é {max(y)}e o menor é {min(y)}')
'''
'''
lista = []
cont = 0
count = 0
for c in range(0,4):
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor == 9:
        cont +=1
    if valor%2 == 0:
        count += 1
print(f'o valor 9 apareceu {cont} vezes.')
if 3 in lista:
    print(f'a primeira aparição do valor 3 foi na {lista.index(3)+1}° posição.')
print(f'{count} foi a quantidade de valores pares .')
'''
'''
produtos = ('notebook' , 7000.00 ,'celular' , 2000.00, 'relógio',1500.00,'Mochila',300.00,'Fones',189.00)
cont = 0
count = 1
print('-'*35)
print('Lista de Preços:')
print('-'*35)
pass

for x in range(0,5):
    print(f'{produtos[cont]}-------->R$:{produtos[count]}')
    cont += 2
    count += 2
    if cont > 8:
        cont = 0
    if count > 10 :
        count = 0


print('_'*35)
'''

tupla = ('Zebra','Hipopotamo','Macaco','Rinoceronte','Javali','Elefante')
for x in tupla:
    print(f'palavra: {x.upper()} \nVogais:')
    for letra in x :
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('\n')






