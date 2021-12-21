'''
x = float(input('Digite o valor da primeira  reta:'))
y = float(input('Digite o valor da segunda reta: '))
z = float(input('Digite o valor da terceira reta :'))
if x < y + z and y < z + x and z < x + y :
    print('As retas atendem a condição para formar um triangulo.')
    if x == y and y == z:
        print('Esse triangulo é equilátero.')
    if x == y and z != y or x == z and y != x or y == z and x != z :
        print('Esse triangulo é isósceles.')
    if x != y and y!= z  and  x != z :
        print('Esse triangulo é escaleno.')
else:
    print('Essas retas não podem formar uma triangulo.')
'''
'''
x = float(input('Digite seu peso:'))
y = float(input('Digite sua altura:'))
imc = x/(y*y)
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc > 18.5 and imc < 25 :
    print('Você está no peso ideal:')
elif imc >= 25 and imc <= 30:
    print('Você está sobrepeso:')
elif imc > 30 and imc <= 40:
    print('Você está obeso:')
else:
    print('tu ta gordo pra cacete:')
'''
'''
pro = float(input('Digite o valor do produto R$:'))
va = str(input('Escolha a forma de pagamento.\n(1) à vista no dinheiro/cheque[10% de desconto].'
      '\n(2) à vista no cartão [5% de desconto].\n(3) em até 2x no cartão[preço normal] '
           '\n(4) em até 3x no cartão[20% de juros'))
if va == '1':
    pr = (pro*10)/100
    print(f'O desconto foi aplicado. o novo valor é de {pro-pr}.')
if va == '2':
    pr1 = (pro*5)/100
    print(f'O desconto foi aplicado. o novo valor é de {pro-pr1}.')
if va == '3':
    pr2 = (pro/2)
    print(f'Duas parcelas de {pr2} e o valor total foi {pro}.')
if va == '4':
    pr3 =(pro/3)
    print(f'Tres parcelas de {pr3}e o valor total foi {pro}.')
elif va not in '1234':
    print('Erro!!! opção invalida.')
'''
'''
import random
j = input('Digite pedra ,papel ou tesoura.')
lis = ['pedra','papel','tesoura']
p = random.choice(lis)

if j == p :
    print('\033[1;33m EMPATE')
elif j == 'pedra'and p == 'tesoura' or j == 'papel' and p == 'pedra' or j == 'tesoura' and p == 'papel':
    print('\033[1;32m VOCÊ GANHOUUU!!!')
elif j == 'tesoura' and p == 'pedra' or j == 'pedra' and p == 'papel'or j == 'papel' and p == 'tesoura':
    print('\033[1;31m VOCÊ PERDEU!!!')
else:
    print('Opção invalidade , tente denovo')
'''
x = 'curso de python no cursoemvideo'
print(x[:5])