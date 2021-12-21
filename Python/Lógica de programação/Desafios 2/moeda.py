def moeda(n):
    return (f'R${n}')

def resumo(n,p,k):
    tam = len('Resumo Do valor')
    print('-='*tam)
    print('       RESUMO DO VALOR')
    print('-='*tam)
    print(f'Preço analisado:  {moeda(n)}')
    print(f'Dobro do  preço:  {dobro(n,True)}')
    print(f'Metade do preço:  {metade(n,True)}')
    print(f'{p}% de aumento:   {aumentar(p,n,True)}')
    print(f'{k}% de redução:   {diminuir(k,n,True)}')
    print('-='*tam)



def aumentar(p,n,d=False):
    if d == False:
        return ((p/100)*n)+n
    else:
        return (f'R${((p/100)*n)+n}')


def diminuir (k,n,d=False):
    if d == False:
        return n-((k/100)*n)
    else:
        return (f'R${n-((k/100)*n)}')


def dobro(n,d=False):
    if d == False:
        return n*2
    else:
        return (f'R${n*2}')


def metade(n,d=False):
    if d == False:
        return n/2
    else:
        return (f'R${n/2}')

