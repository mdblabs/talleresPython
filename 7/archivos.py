"""

Formas de abrir un archivo de texto plano

Modos de abrirlo:
r, read
w, write
a, append al final del archvio
b, binario
+, lectura y escritura simultanea

"""

# Lee archivo de texto completo y lo guarda en string
archivo=open('hola.txt','r')    
completo=archivo.read()
print completo

print '*************************'

# Lee archivo linea a linea cada vez que llama a readline
# Y lo guarda cada linea en un string
archivo=open('hola.txt','r')
linea=archivo.readline()
print linea
#archivo.seek(2)
linea=archivo.readline()
print linea
linea=archivo.readline()
print linea

print '*************************'

# Lee todo el archivo y lo guarda cada linea en un elemento de
# una lista
archivo=open('hola.txt','r')      
vector=archivo.readlines()
print vector

print '*************************'
