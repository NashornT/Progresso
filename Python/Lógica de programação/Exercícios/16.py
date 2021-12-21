'''
count = 0
M = 0
m = 0
p = input('Deseja entrar no programa:(S/N) ').strip().upper()[0]
while p == 'S' :
    if p == 'S':
        i = int(input('Digite a idade: '))
        s = input('Digite o sexo:(M/F) ').strip().upper()[0]
        if s not in 'MF':
            s = input('Digite o sexo:(M/F) ').strip().upper()[0]
        if i > 18 and s == 'M':
            count += 1
        if s == 'M':
            M += 1
        if i > 20 and s == 'F':
            m += 1
        p = input('Deseja continuar:(S/N) ').strip().upper()[0]
    if p == 'N':
        break
print(f'De acordo com a pesquisa , {M} homens foram cadastrados desses '
      f'\n, {count} tem 18 anos e {m} mulheres tem mais de 20 anos .')
'''
'''
p = input('Deseja entra no programa:(S/N) ').upper()
preco = []
nomes = []
cont = 0
count = 0
menor = None
indice = None
while p == 'S':
   n = input('Digite o nome do produto: ')
   pre = float(input('Digite o preço: '))
   nomes.append(n)
   preco.append(pre)
   p = input('Deseja continuar :(S/N) ').upper()
   for x in range (0, len(nomes)):
       if menor is None or preco[x] < menor:
           menor = preco[x]
           indice = x

   if pre > 1000 :
       cont += 1
   if p == 'N':
       break

print(f'O total de gastos foi de {sum(preco)} ,\n sendo que {cont} custam mais de 1000 R$ '
      f'\n e o mais barato deles é o {nomes[indice]} e custa {min(preco)} ')
'''
p = input('Deseja entrar no caixa eletronico (S/N):').upper()
n10 = 0
n50 = 0
n20 = 0
n1 = 0
while p == 'S':
    caixa = []
    print('Iniciando caixa...')
    valor = int(input(('Digite o valor que gostaria de sacar:')))
    notas = int(input('Gostaria de sacar em notas de 50,20,10 ou 1 ?? '))
    if valor == 0:
        print('valor invalido!!')
    if valor > 10000:
        print('Limite atingido.')
        break
    if notas == 50:
        print(f'{valor / 50} notas de R$50.00 estão sendo enviadas !!')
        break
    if notas == 20:
        print(f'{valor / 20} notas de R$20.00 estão sendo enviadas !!')
        break
    if notas == 10:
        print(f'{valor / 10} notas de R$10.00 estão sendo enviadas !!')
        break
    if notas == 1:
        print(f'{valor} notas de R$1.00 estão sendo enviadas !!')
        break







    





