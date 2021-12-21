'''
frase = input('Digite seu nome completo: ')
frase2 = int(len(frase))
print(frase.upper())
print(frase.lower())
print(frase2-5)
print(len(frase[0:7]))
'''
#1234
'''
num = input('Digite um número:')
mi = num[0:1]
ce = num[1:2]
de = num[2:3]
un = num[3:4]

print(f'unidade:{un} \ndezena:{de} \ncentena:{ce} \nmilhar:{mi} ')
'''
'''
cid = input('Digite o nome da sua cidade:').upper()
if cid.startswith('SANTO') :
    print('Sua cidade  começa com Santo.')
else:
    print('Sua cidade não começa com Santo')
'''
'''
nom = input('Digite seu nome completo:').upper()
if 'SILVA' in nom:
    print('Seu nome tem silva.')
else :
    print('Seu nome não tem silva.')
'''
'''
fra = str(input('Digite o seu nome completo:')).split()

print(f'Seu primeiro nome é {fra[0]}.')
print(f'Seu ulitmo nome é {fra[len(fra)-1]}')
'''
'''
N = input('Digite aqui:').upper()
print(N.find('A'))
print(N.rfind('A'))
'''