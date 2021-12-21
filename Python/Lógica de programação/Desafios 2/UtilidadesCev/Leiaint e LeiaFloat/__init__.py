def leiaint():
    try:
         k = int(input('DIgite um número inteiro:'))
    except:
        while True:
            print('Ocorreu um erro.')
            r = input('Digte um número inteiro:')
            if r.isnumeric():
                print(f'Muito  Obrigado. você digitou o número {r}')
                break
    else:
        print(f'Muito Obrigado. você digitou o número {k}')

def leiafloat():
    try:
       k =  float(input('DIgite um número real:'))
    except:
        while True:
            print('Ocorreu um erro.')
            r = input('Digte um número real:')
            if r[0].isnumeric():
                print(f'Muito  Obrigado. vc digitou o real {r}')
                break
    else:
        print(f'Muito Obrigado. você digitou o real {k}')

def resumo():
    leiaint()
    leiafloat()
resumo()

