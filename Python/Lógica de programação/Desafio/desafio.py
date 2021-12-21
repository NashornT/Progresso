
''' nascimento = ano- idade '''
#imc= peso/(altura*altura)

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
idade = int(input('Digite sua idade: '))
altura =float(input('Digite sua altura: '))
ano = 2021
nascimento = ano-idade-1
imc = peso / (altura*altura)

print(f'{nome} tem {idade}  anos de idade ,{altura} de altura e pesa {peso}kg')
print(f'nasceu em {nascimento}.')
print(f'Seu imc é {imc})')
