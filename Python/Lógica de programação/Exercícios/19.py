'''
l1 = []
l2 = []
count = 0
while True:
    nome =str(input('Nome: '))
    peso = int(input('Peso: '))
    l1.append(nome)
    l2.append(peso)
    count += 1
    p = input('Deseja continuar?? (S/N) ').strip().upper()[0]
    if p == 'N':
        break

print('-='*30)
print(f'Foram cadastradas {count} pessoas.')
print(f'O maior peso foi de  {l1[l2.index(max(l2))]} com {max(l2)}KG  ')
print(f'O menor peso foi de {l1[l2.index(min(l2))]} com {min(l2)}KG ')
print('-='*30)
'''
'''
lista = []
pares = []
impares = []
for x in range(0,7):
    num = int(input('Digite um valor:'))
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(sorted(pares))
print(sorted(impares))
'''
'''
lista = []
pares = []
li = []
l2 = []
count = 0
cont = 0
n = 0
n1 = 4

for x in range(0,9):
    val = int(input(f'Digite o valor [{count},{cont}] da matriz: '))
    lista.append(val)
    cont += 1
    if cont == 3:
        cont = 0
        if count == 1:
            count = 2
            count -=1
        count += 1
    if val%2 == 0:
        pares.append(val)

for c in range(0,3):
    print(f'{[lista[n]]}{[lista[n+1]]}{[lista[n+2]]}')
    n += 3

li.append(lista[2])
li.append(lista[5])
li.append(lista[8])
l2.append(lista[3])
l2.append(lista[4])
l2.append(lista[5])

print('-='*35)
print(f'A soma dos valores pares é {sum(pares)}')
print(f'A soma dos valores da  terceira coluna é {sum(li)}')
print(f'O maior valor da segunda linha é {max(l2)}')
print('-='*35)
'''
'''
import random
lis = []
num = []
count = 0
n1 = 0
for c in range(1,61):
    lis.append(c)
n = int(input('Quantos jogos quer que sorteie ?? '))
print(f'Sorteando {n} jogos')
for x in range(0,n):
    for c in range(0,6):
        num.append(random.choice(lis))
        if num[count] is not None:
            count +=1
        if num[count] 
'''

lista = []
nomes = []
notas = []
count = 1
n = 0
n1 = 1
n2 = 0
n3 = 0
while True:
    nom = input('Nome: ')
    not1 = float(input('Nota1: '))
    not2 =float(input('Nota2: '))
    nomes.append(nom)
    notas.append(not1)
    notas.append(not2)
    p = input('Deseja continuar ?? (S/N) ').strip().upper()[0]
    if p == 'N':
        break

for x in range(0,len(nomes)):
    print(f'O {count}° foi {nomes[n]} com média de {(notas[n3]+notas[n3+1])/2}')
    count +=1
    n += 1
    n3 += 2
while True:
    d = input('Deseja ver as notas de algum aluno separado?? (S/N)').strip().upper()[0]
    if d == 'N':
        break
    else:
        p2 = int(input('Digite o número da ordem do aluno que deseja ver a nota'))
        if p2 == n1 :
            print(f'As notas são [{notas[n2]},{notas[n2+1]}]')
            n2 += 2
            n1 += 1

