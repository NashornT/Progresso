num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze'
       ,'quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
dig = int(input('Digite um número de 0 a 20: '))
while dig < 0 or dig > 20:
    print('\033[31mErro\033[m !! valor invalido')
    dig = int(input('Digite um número de 0 a 20: '))
if dig == 0:
    print(f'você escolheu o número zero')
if dig == 1:
    print(f'você escolheu o número um')
if dig == 2:
    print(f'você escolheu o número dois')
if dig == 3:
    print(f'você escolheu o número tres')
if dig == 4:
    print(f'você escolheu o número quatro')
if dig == 5:
    print(f'você escolheu o número cinco')
if dig == 6:
    print(f'você escolheu o número seis')
if dig == 7:
    print(f'você escolheu o número sete')
if dig == 8:
    print(f'você escolheu o número oito')
if dig == 9:
    print(f'você escolheu o número nove')
if dig == 10:
    print(f'você escolheu o número dez')
if dig == 11:
    print(f'você escolheu o número onze')
if dig == 12:
    print(f'você escolheu o número doze')
if dig == 13:
    print(f'você escolheu o número treze')
if dig == 14:
    print(f'você escolheu o número quatroze')
if dig == 15:
    print(f'você escolheu o número quinze')
if dig == 16:
    print(f'você escolheu o número dezesseis')
if dig == 17:
    print(f'você escolheu o número dezesete')
if dig == 18:
    print(f'você escolheu o número dezoite')
if dig == 19:
    print(f'você escolheu o número dezenove')
if dig == 20:
    print(f'você escolheu o número vinte')

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    num3 = int(input('Digite um número: '))
    num4 = int(input('Digite um número: '))
    num5 = int(input('Digite um número: '))
    if num3 < num2:
        li.append(num3)
        li.append(num2)
    else:
        li.append(num2)
        li.append(num3)
    if num5 < num4:
        li.append(num5)
        li.append(num4)
    else:
        li.append(num4)
        li.append(num5)
    if num3 > num5:
        print(li)