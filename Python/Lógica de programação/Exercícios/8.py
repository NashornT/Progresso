'''
carteira = int(input('Deposite um valor :'))
conv = carteira // 3.27
x = input('Deseja converter para dolar : Y/N ').upper()
if x.startswith('Y'):
    print(f'Seu dinherio foi convertido em {conv} dolares ')
else :
    print(f'Saindo do programa.')
'''
'''
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a alutra da parade : '))
area = largura * altura
tinta = area / 2
print(f'A quantidade de tinta total para pintar essa parede é {tinta}.')
'''
'''
x = float(input('Digite o preço do produto:R$ '))
pr = (x * 5) /100
y = x - pr

print(f'O desconto foi aplicado o novo preço é {y}')
'''
'''
x = float(input('Digite o seu salário'))
pr = (x * 15)/100
y = x + pr
print(f'Seu novo salário é {y}')
'''

C = float(input('Digite a temperatura em °C: '))
K = 273 + C
F = (C * 1.8) + 32
print(f'A temperatura em F e K é {F} °F, {K}K')