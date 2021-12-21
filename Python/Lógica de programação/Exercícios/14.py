'''
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a  razão: '))
n = 0
print('--------')
while n < 10 :
    n += 1
    if n == 0:
        print(a1, end='--')
    if n != 0:
        print(a1+(n-1)*r)
print('--------')
c = 'S'
while c == 'S':
    c = input('Deseja mostrar mais alguns termos: (S/N) ').upper()
    if c == 'S':
        p = int(input('Quantos??'))
        if p == 0:
            break
        for x in range(a1,a1+(p*r),r):
            print(x)
'''
'''
n = 0
count = 0
li = []
while n != 999:
   if n >= 999:
       print('\033[031mInvalido , você ultrapassou o limite\033[m ')
       break
   if n != 999:
       n = int(input('Digite um número inteiro:'))
       if n == 999:
           break
       count += 1
       li.append(n)
print(f'a quandtidade de números digitados foi \033[33m{count}\033[m,'
      f'\ne sua soma é \033[33m{sum(li)}\033[m')
'''
'''
count = 0
li = []
while True:
    n = int(input('Digite um número inteiro: '))
    count += 1
    li.append(n)
    p = input('Deseja continuar(S/N): ').upper()
    if p == 'S':
            continue
    if p == 'N':
            break

    if n < 0 :
        break
print(f'A média foi {sum(li)/count} e os valores máximo e minimo são '
      f', respectivamente {max(li)} , {min(li)} ')
'''
