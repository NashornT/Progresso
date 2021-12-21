
cedo= 11
tarde= 13
noite= 19

hora =int(input('Que horas são ? '))


if hora <= cedo :
      print('Bom dia !!')

elif hora >= cedo  and hora <= noite:
    print('Boa tarde !!')

elif hora >= noite   :
    print('Boa noite !!')


