# -*- coding: cp1252 -*-
""" Tipos de variables """

""" int, 32 (o 64bits) de precision,
    long, entero de precision infinita
    real, de 64 bits de precision """

a=12345
b=687454678654356754345676567667676667L
c=6.0

#print a.bit_length()
#print type(c)


""" string, tiene métodos de sumar otras cadenas, pasar a maysculas... etc"""

cad1="hola"
cad2="mundo"
result=cad1+" "+cad2
#print result

res=cad2.capitalize()
#print res


""" vectores, o listas """

vec=[1,3,4.0,5,"hola",[5,6,9]]

matrix=[[1,2,3],[4,5,6],[7,8,9]]

#vec.reverse()
#vec.remove(4.0)
#vec.pop()
#vec.sort()
#vec.insert(0,77)
#vec[0]=35

#print vec
#print vec[1:]



""" tuplas """

tupl=4,5,6
#print tupl


""" diccionarios """

varrr=999
dicc={varrr:"hola", 24:5}

etiq={"nombre":"pepe", "pass":1212}

#print dicc


""" booleanos """
var=True   #1
var2=False  #0
rr=var*var2
#print rr
#print(-1)*(+1)
#print 2**4

""" Comparadores """
#<=
#>=
#==
#!=  si distinto, true
#<>  si distinto, true

""" Operadores """
#print 21%5    #resto de division
#print 21**3   #elevar a una potencia

#print (2*3+5*2)/2.+5   #orden de operaciones
