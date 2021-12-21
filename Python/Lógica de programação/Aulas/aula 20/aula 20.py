'''
For / else em python
'''

#variavel = ['Barboza' , 'Gustavo', 'Silva']

#for valor in variavel :
   #print(valor)

'''for valor in variavel :
    if valor.startswith('G'):
        print(f'{valor} Começa com G')
    else :
        print(f'{valor} Não começa com G')'''
'''x = False
for valor in variavel :
    if valor.startswith('G'):
        x = True
    if x :
        print('Existe palavra que começa com G')
    else:
        print('Não existe uma palavra que começa com G ')'''

'''Segunda parte 
Split , Join, Enumerate 
* Split - Dividir  uma string #str 
*Join - Juntar uma lista #str
*Enumerate - Enumerar elementos da lista #list
'''

'''string = 'O Brasil é o pais do futebol , o Brasil é penta. '
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1 :
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase .')
'''

'''
string = 'O Brasil é o pais do futebol , o Brasil é penta. '
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})x ')
'''

'''
string = 'O Brasil é o pais do futebol , o Brasil é penta. '
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)
'''


lista = [ 'arroz', 'fejão', 'batata']
n1, n2, n3 =lista

print(n2)

