'''
y = input('digite seu nome :')
j = y
07/12/1999
0123456789
for x in range(0,len(y)+1,) :
    print(j[0:x])
'''
meses = ["janeiro",
         "fevereiro",
         "março",
         "abril",
         "maio",
         "junho",
         "julho",
         "agosto",
         "setembro",
         "outubro",
         "novembro",
         "dezembro"]

data = input("informe a data (dd/mm/aaaa): ")


print (data.split("/")[0],
       "de",
       meses[(int(data.split("/")[1])-1)],
       "de",
       data.split("/")[2])


