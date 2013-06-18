""" BUCLES """

#Bucle IF
"""
var1=2
var2=3

if (var1>var2) :
    print "var1 mayor que var2"
elif var1==var2:
    print "var1 no es mayor que var2 y son iguales"
else:
    print "no es mayor ni es igual"

"""


#Bucle FOR
"""

#iteramos en una secuencia
secuencia=['uno', 2, 'tres']   

#itereamos sobre las posiciones del 0 al 999
listaelem=range(0,1000)

for el in listaelem:
    print el


#Uso del break y continue
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]
    if a[i] == 'a':
        break


for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
    continue
    print "Found a number", num
    
"""

#Bucle WHILE

contador=5
while contador:
    contador=contador-1;
    print contador






