"""

El programa esperara un parametro en el momento de ejecucion,
bien el nombre de un archivo, una valor de una variable, etc.

Para incluir un parametro, se ejecutara el programa desde
la consola de Windows (O Unix) con formato:

'python nombreprograma.py nombrevariable1'

Se podra gestionar en el caso de que no haya ningun parametro
en el momento de ejecutar programa (Si la variable sys.argv
no es mayor que uno, significa que no hay parametro)
y que ejecute un codigo por defecto.

"""

import sys

def main():

    #sys.argv[0] el nombre del programa
    #sys.argv[1] el primer parametro
    #sys.argv[2] el segundo ...

    print 'nombre programa ', sys.argv[0]
    
    if(len(sys.argv) > 1):
        
        print 'abrir: ' + sys.argv[1]
        nombrearchivo=sys.argv[1]
    else:
        print 'archivo cargado por defecto'
        nombrearchivo="hola.txt"

    #nombrearchivo=raw_input("dime nombre de archivo")
    
    archivo=open(nombrearchivo,'r')    
    completo=archivo.read()
    print completo    


if __name__ == "__main__":
    main()
