lis = []
dic = {}
count = 0
cont = 1
dic['nome'] = 'Jose'
lis.append(dic['nome'])
dic ['idade'] ='15'
lis.append(dic['idade'])
dic.clear()
dic['nome'] = 'Gustavo'
lis.append(dic['nome'])
dic ['idade'] ='16'
lis.append(dic['idade'])
for x in lis:
    print(f'{lis[count]}----->{lis[cont]}')
    count += 2
    cont += 2
    if count > len(lis) or cont > len(lis):
     break




