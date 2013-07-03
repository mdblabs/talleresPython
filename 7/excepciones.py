"""

Gestion de excepciones.
Se utilizara cuando un trozo del programa tiene la posibilidad de
causar un error, que pare el programa, como division por cero,
nombre de archivo no valido, conversion de variable invalida...

"""



try:
    print 'intentando abrir archivo...'
    archivo=open('sadasd.txt','r')    
    completo=archivo.read()
    print completo
except IOError as detalle:
    print 'no existe archivo!',detalle


print '****************************'

a=2
b=0
try:
    print 'intentando operacion de division...'
    operacion=a/b
    print operacion
except ZeroDivisionError:
    print 'division entre cero. Sustituyendo por numero casi cero'
    b=0.0000000001
    operacion=a/b
    print operacion

