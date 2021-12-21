'''
escolha  = input('Escolha uma das opções: F ou M ' )

for x in escolha :
    if escolha.startswith('F') or escolha.startswith('f') :
        print('você escolheu Feminino: ')

    elif escolha.startswith('M') or escolha.startswith('m'):
        print('você escolheu Masculino: ')

    else:
        print('escolha invalida')
'''
'''
letra = input('Digite uma vogal ou uma consoante. ')

if letra.isalpha():
    if letra in 'AaEeIiOoUu':
        print('É uma vogal.')
    else:
        print('É uma consoante.')
if letra.isnumeric():
    print('ERRO')
'''
'''
y = input('Digite uma sequência de 8 números .')
z = (y[::-1])


for x , w  in enumerate(z) :
  print(w,x)
'''
'''
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
print(x + y)
'''
'''
num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num - 1
print(f'Seu sucessor é {sucessor} e seu antecessor é {antecessor}')
'''
'''
num = int(input('Digite um número :'))
do = num * 2
tr = num * 3
po = num ** 2
ra = num **(1/2)

print(f'Seu dobro é {do} \nseu triplo é {tr} \ne sua raiz quadrada é {ra}')
'''
'''
nota1 = int(input('Digite sua primeira nota: '))
nota2 =int(input('Digite sua segunda nota: '))
med = (nota1 + nota2)/2
print(f'Sua média foi {med}')
'''
'''
num = int(input('Digite o qualquer valor em metros:'))
cm = num * 100
mm = num * 1000
print(f'O valor convertido em cm é {cm} e em mm é {mm} .')
'''
'''
num = int(input('Digite um número :'))
tabuada = num *1
tabuada2 = num *2
tabuada3 = num *3
tabuada4 = num *4
tabuada5 = num *5
tabuada6 = num *6
tabuada7 = num *7
tabuada8 = num *8
tabuada9 = num *9
tabuada10 =num *10
print('Sua tabuada é :')
print(tabuada)
print(tabuada2)
print(tabuada3)
print(tabuada4)
print(tabuada5)
print(tabuada6)
print(tabuada7)
print(tabuada8)
print(tabuada9)
print(tabuada10)
'''