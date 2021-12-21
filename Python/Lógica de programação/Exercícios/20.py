'''
dic = {}
dic['nome'] = str(input('Nome: '))
dic['média'] = float(input(f'Média de {dic["nome"]}: '))

print('-='*15)
print(f'Nome é igual a {dic["nome"]}')
print(f'Média igual a {dic["média"]}')
if dic['média'] < 6 :
    print('Situação é \033[31mReprovado\033[m')
else:
    print('Situação é \033[32mAprovado\033[m')
print('-='*15)
'''
'''
import random
import time
dic = {}
count = 0
n = 1
n1 = 1
for x in range(1,5):
    dic[count] = random.randint(1,6)
    print(f'O jogador {n}º tirou {dic[count]}')
    time.sleep(1)
    n += 1
    count += 1
print('Ranking dos Jogadores')
for v in sorted(dic ,key=dic.get,reverse=True):
    print(f'O {n1}° foi {dic[v]}')
    time.sleep(1)
    n1 += 1
'''
'''
dic ={}
for x in range(0,1):
    dic['nome'] = str(input('Nome: '))
    dic['ano'] = int(input('Ano de nascimento: '))
    dic['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
    if dic['ctps'] == 0:
        break
    dic['contratação'] = int(input('Ano da contratação: '))
    dic['salário'] =int(input('Salário:R$ '))
for x in range( 0,1):
    print(dic)
    print(f' nome tem o valor {dic["nome"]}')
    print(f' idade tem o valor {2021-dic["ano"]} ')
    print(f' ctps tem o valor {dic["ctps"]}')
    if dic['ctps'] == 0:
        break
    print(f'contratação tem  o valor {dic["contratação"]} ')
    print(f'salário tem o valor {dic["salário"]}')
    print(f'aposentadoria tem o valor {(dic["contratação"]-dic["ano"])+30}')
'''
'''
dic = {}
gols = []
n = 0

dic['nome'] = str(input('Nome do Jogador: '))
dic['partidas'] =int(input(f'Quantas partidas {dic["nome"]} jogou? '))
count = dic['partidas']
for x in range(1,count+1):
    g = int(input(f'Quantos gols na partida {x}° '))
    gols.append(g)
dic['gols']=gols
dic['total'] = sum(gols)
print('-='*30)
print(dic)
print('-='*30)
print(f'O campo nome tem  o valor {dic["nome"]}. ')
print(f'O campo gols tem o valor {dic["gols"]}.')
print(f'O campo total tem o valor {dic["total"]}.')
print('-='*30)
print(f'O jogador {dic["nome"]} jogou {dic["partidas"]} partidas.')
for y in range(1,count+1):
    print(f'=> Na partida {y}° , fez {gols[n]} ')
    n += 1
print(f'Foi um total de {dic["total"]} gols.')
'''
lista = []
dic = {}
con = 0
li = []
life = []
ve = []
while True:
    dic['nome'] = str(input('Nome: '))
    dic['sexo'] = str(input('sexo:(M/F)')).strip().upper()[0]
    dic['idade'] = int(input('Idade:'))
    p = str(input('Quer continuar ?? (S/N) ')).strip().upper()[0]
    con += 1
    lista.append(dic.copy())
    li.append(dic['idade'])
    if dic['sexo'] =='F':
        life.append(dic['nome'])
    if p =='N':
        break
if dic['idade'] > sum(li)/con:
    ve.append(dic['nome'])
print(lista[0]['nome'])
print('-='*30)
print(f'- O grupo tem {con} pessoas. ')
print(f'- A média de idade é de {sum(li)/con}')
print(f'- As Mulheres cadastradas foram: {life} ')
print(f'- Lista de pessoas que estão acima da média:')
print(f'{ve}')
