'''
import random
l1 = int(input('Tente adivinhar o número de 0 a 5:'))
l2  =[0,1,2,3,4,5]
ls = random.choice(l2)
if l1 == ls :
    print(f'Você acertou !! o numero {l1} é oq eu estava pensando:')
else:
    print(f'Uma pena! você não acertou:')
'''
'''
ve = int(input('Digite a velocidade que você trafegava em km/h:'))
multa = ve*7
if ve > 80:
    print(f'Você foi multado \nsua multa é de {multa}R$.')
elif ve == 80:
    print('Atenção, você estava trafegando muito proximo do limite.')
else:
    print('Estava dentro do limite estabelecido.')
'''
'''
n = int(input('Digite um número:'))
if n%2 == 0:
    print('Esse número é par.')
else:
    print('Esse número é impar:')
'''
'''
v = float(input('Digite a distância da viagem em KM:'))
v1 = v*0.5
v2 = v*0.45
if v > 200:
    print(f'O valor de sua viagem é {v2}R$.')
else:
    print(f'O valor de seu viagem é {v1}R$.')
'''
'''
ano = int(input('Digite um ano:'))
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0 :
   print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto')
'''
'''
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número'))
if n3 > n2 and n3 > n1 :
    print(f'O maior número é esse {n3}.')
elif n2 > n3 and n2 > n1:
    print(f'O maior número é esse {n2}.')
elif n1 > n3 and n1 > n2 :
    print(f'O maior número é esse {n1}.')

if n3 < n2 and n3 < n1:
    print(f'O menor número é esse {n3}.')
elif n2 < n3 and n2 < n1 :
    print(f'O menor número é esse {n2}.')
elif n1 < n3 and n1 < n2 :
    print(f'O menor número é esse {n1}.')

if n3 == n2 or n2 == n1 or n3 == n1 :
    print('Por favor digite valores diferentes.')
'''
'''
sa = float(input('Digite seu sálario:'))
if sa > 1250:
    print(f'o seu aumento foi de 10% seu novo sálario é {(sa*10)/100}R$')
if sa == 1250 or sa < 1250 :
    print(f'Seu aumento foi de 15% seu novo sálario é {(sa*15)/100}R$')
'''
l1 = int(input('Digite o valor do primeiro segmento de reta:'))
l2 = int(input('Digite o valor do segundo segmento de reta:'))
l3 = int(input('Digite o valor do terceiro segmento de reta:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Essa retas podem formar um triangulo.')
else:
    print('Essa reta não podem formar um triangulo:')
