'''
li = []
for x in range(0,5):
    num = int(input('Digite um valor:'))
    li.append(num)
for i,n in enumerate(li):
    print(f'o {i+1}° foi o {n}')
print(f'o maior valor foi {max(li)}\n'
      f' o menor valor foi {min(li)}')
'''
'''
li = []
while True:
    num = int(input('Digite um valor: '))
    p = input('Deseja continuar ?? (S/N)').strip().upper()[0]
    if p == 'N':
        break
    if num not in li :
        li.append(num)
print('--'*10)
print(sorted(li))
print('--'*10)
'''
'''
li = []
count = 0
n5 = 0
while True:
    num = int(input('Digite um número: '))
    li.append(num)
    count += 1
    p = input('Deseja continuar?? (S/N) ').strip().upper()[0]
    if p == 'N':
        break
    if num == 5:
        n5 += 1

print(f'Esse foi o total de números digitados: {count}')
li.sort(reverse=True)
print(li)
if 5 in li :
    print(f'O valor 5 foi digitado {n5} vez(es).')
else:
    print(f'O valor 5 não foi digitado.')
'''
'''
l1 = []
lp = []
li = []
while True:
    num =int(input('Digite um valor: '))
    l1.append(num)
    p = input('Deseja continuar ?? (S/N) ').strip().upper()[0]
    if num%2 == 0:
        lp.append(num)
    else:
        li.append(num)
    if p == 'N':
        break
print('=-'*30)
print(f'Lista total:\n{l1}')
print('=-'*30)
print(f'Lista de valores pares:\n{lp}')
print('=-'*30)
print(f'Lista de valores impares:\n{li}')
print('=-'*30)
'''
ex = input('Digite a expressão: ')
count = 0
for x in ex:
    if x == '(':
        count += 1
    elif x == ')':
        count -= 1
    if count < 0:
        break
if count == 0 :
    print('Expressão valida.')
else:
    print('Expressão invalida.')

