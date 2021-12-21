'''
ca = float(input('Digite o valor da casa:'))
sa = float(input('Digite o salário do comprador R$:'))
an = float(input('Digite em quantos anos pretende pagar:'))
prest = ca/an
sa1 = (30*sa)/100
if prest > sa1:
    print('\033[1;31m O emprestimo foi negado.\033[1;31m ')
else:
    print('\033[1;32m O emprestimo foi aparovado.\033[1;32m ')
'''
'''
l =int(input('Escreva um número inteiro que deseja converter:'))
l1 = int(input('Digite \033[1;32m 1 para binário'
               ' \033[1;32m , \033[1;31m  2 para octal\033[1;31m  '
               'e \033[1;33m 3 para hexacedimal\033[1;33m :'))


if l1 == 1:
    x = str(bin(l))
    print(x)
elif l1 == 2:
    y = str(oct(l))
    print(y)
elif l1 == 3:
    z = str(hex(l))
    print(z)
'''
'''
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
if n1 > n2 :
    print('O \033[1;31m primeiro \033[1;31m '
          ' valor é'
          '\033[1;36m maior\033[1;36m .')
elif n2 > n1:
    print('O \033[1;33m segundo \033[1;33m  valor é \033[1;32m maior\033[1;32m .')
elif n2 == n1:
    print('Não exite valor \033[1;35m maior \033[1:35m, os dois são \033[1;34m iguais \033[1;34m.')
'''
'''
an = int(input('Digite o ano de seu nascimento:'))
x = 2021 - an
if x > 18 :
    print(f'Seu periodo de alistamento já passou.')
elif x == 18 :
    print(f'Está na hora de se alistar.')
else :
    print(f'Você ainda não pode se alistar.')
y = x - 18
if an < 2003:
    print(f'o prazo ja passou faz {y} ano(s).')
elif an > 2003:
    if y < 0 :
        print(f'ainda falta(m) {y.__abs__() } ano(s) para o alistamento.')
'''
'''
p = float(input('Digite sua nota de portugues:'))
m = float(input('Digite sua nota de matemamtica:'))
med = (p + m)/2
if med < 5.0:
    print('\033[1;31m REPROVADO \033[1;31m')
elif med > 5.0 and med < 6.9 :
    print('\033[1;33m RECUPERAÇÃO \033[1;33m')
else:
    print('\033[1;32m APROVADO \033[1;32m')
'''
'''
id = int(input('Digite sua idade:'))
if id <= 9:
    print('Sua categoria é:\033[1;34m MIRIM')
elif id > 9 and id <= 14 :
    print('Sua categoria  é:\033[1;34m INFANTIL')
elif id > 14 and id <= 19:
    print('Sua categoria é:\033[1;34m JUNIOR')
elif id >=19 and id <= 20:
    print('Sua categoria é:\033[1;34m SENIOR')
else :
    print('Sua categoria é:\033[1;34m MASTER')
'''




