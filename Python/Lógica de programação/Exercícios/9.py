'''
num = float(input('Digite um número:'))
num1 = int(num)
print(f'{num1}')
'''
'''
num = int(input('Digite um cateto: '))
num2 = int(input('Digite outro cateto: '))
hi = num**2 + num2**2
hip = hi**(1/2)

print(f'A hipotenusa é {hip}')
'''
'''
import math
num = float(input('Digite um angulo: '))
cos = math.cos(math.radians(num))
sen = math.sin(math.radians(num))
tang = math.tan(math.radians(num))
print(f'seu seno é {sen} \nseu cosseno é {cos} \ne sua tangente é {tang}')
'''
'''
import random
nom1 = input('Digite um nome:')
nom2 = input('Digite um nome:')
nom3 =input('Digite um nome:')
nom4 =input('Digite um nome: ')
list = [nom1,nom2,nom3,nom4]
lista = random.choice(list)
print(f'O escolhido foi {lista}')
'''
import random
nom1 = input('Digite o nome de um aluno: ')
nom2 = input('Digite o nome de um aluno: ')
nom3 = input('Digite o nome de um aluno: ')
nom4 = input('Digite o nome de um aluno: ')
list= [nom1,nom2,nom3,nom4]
list1 =[1,2,3,4]
lista = random.choice(list)
lista2= random.choice(list1)
print(f'O aluno escolhido foi {lista} e sua ordem foi {lista2}°')