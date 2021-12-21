x = input('Digite uma frase:')
y = input('Digite outra frase:')

TX = len(x)
TY = len(y)

print(f'String 1: {x}')
print(f'string 2: {y}')

print(f'Tamanho de "{x}":{TX} caracteres')
print(f'Tamanho de "{y}":{TY} caracteres')

if TX != TY :
 print('As strings são de tamanhos diferentes.')
elif TX == TY :
 print('As strings são de tamanhos iguais.')


if x == y :
       print('As strings possuem o mesmo conteúdo.')
elif x != y:
     print('As strings possuem conteúdos diferentes.')

