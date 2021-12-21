'''
Operadores Relacionais
== igualdade > maior que
>= maior que ou igual a
< menor que
<= menor que ou iguala
!= diferente
'''
num_1 = 2
num_2 = 2

var1 = 'Gustavo'
var2 = 'Barboza'

idade_menor =20
idade_maior = 30
'''
print(num_1 == num_2)
'''
#print(num_1 > num_2)

#print(var1 != var2)

nome =input('Qual o seu nome ?')
idade = input('Qual a sua idade ?')
idade= int(idade)

if idade >= idade_menor and idade<= idade_maior:
    print(f'{nome} pode pegar o empréstimo .')
else:
    print(f'{nome} Não pode pegar o empréstimo .')
