from Uteis.Leitor import  *
from time import sleep
if arquivoexiste('teste'):
    print('Arquivo encontrado com sucesso !!')
    print('ACESSANDO ARQUIVO...')
    sleep(1)
    lerarquivo('teste')
else:
    print('Não foi possivel encontrar o arquivo.')
    print('CRIANDO ARQUIVO...')
    sleep(1)
    criararq(input('Nome:'))





