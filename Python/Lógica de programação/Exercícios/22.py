'''
def voto(ano):
    opc = str('VOTO OPICONAL')
    obr = str(' VOTO OBRIGATÓRIO')
    nega = str('VOTO NEGADO')

    if 2021-ano == 16 or 2021-ano == 17 or 2021-ano >= 65:
        return opc
    elif 2021-ano < 16 :
        return nega
    elif 2021-ano >= 18 and 2021-ano < 65:
        return obr



idade = int(input('Digite o ano de seu nascimento: '))
print(f'com {2021-idade} :{voto(idade)}')
'''
'''
def ficha(a='desconhecido',b=0):
    print(f'o jogador {a} teve um total de {b} gols.')


nome = str(input('Nome: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(b=gols)
else:
    ficha(nome,gols)
'''
'''
def leiaint(n):
    if n.isnumeric():
        print(f'\033[32mValor aprovado , Você digitou um número {n}..\033[m')
    elif n in '´~;.,><^`:/?}}{{[]-_=+*&¨%$#@!"\|'or n.isalpha() or n in '      ':
        while True:
            if n.isalpha() or n in '´~;.,><^`:/?}}[]{{-_=+*&¨%$#@!"\|'or n in '        ':
                print('\033[31mERRO , tente denovo\033[m')
                n = input('Digite um número: ')
            else:
                print(f'\033[32mValor aprovado , Você digitou o número {n}..\033[m')
                break
h = leiaint(input('Digite um número:'))
'''
"""
dic = {}
lis = []
def notas(a,b,c,d=False):
    '''
    ->Função para analisar notas e situação de vários alunos.
    :param a:Primeira Nota
    :param b:Segunda Nota
    :param c:Terceira Nota
    :param d:Utilizado para amostrar a situação , True para aparecer , False para esconder
    :return:None
    '''
    lis.append(a)
    lis.append(b)
    lis.append(c)
    dic['Total'] = len(lis)
    dic['Maior'] = max(lis)
    dic['Menor'] = min(lis)
    dic['Média'] = (a+b+c)/3
    if d == True:
        if dic['Média'] <= 7.5:
            dic['Situação'] = 'Boa'
        if dic['Média'] >= 8:
            dic['Situação'] = 'Excelente'
        if dic['Média'] <= 6:
            dic['Situação'] = 'Razoável'
        if dic['Média'] < 6:
            dic['Situação'] ='Pessimo'
    else:
        None
help(notas)
"""
cores = ('\033[m','\033[1;41m','\033[1;42m','\033[1;43m','\033[1;44m','\033[1;107m')
def ajuda(com):
    titulo(f'Entrando no Manual...\'{com}\'',2)
    print(cores[5], end='')
    help(com)
    print(cores[0])
def titulo(msg,cor=0):
    tam = len(msg)
    print(cores[cor], end='')
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(cores[0], end='')

comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp',1)
    comando = str(input('Função ou Biblioteca ??'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO',3)
