""" Funciones """

def suma(var1, var2):
    result=var1+var2
    return result

def otrafun():
    print "hola"

def main():
    print "Este es mi codigo principal"
    print "llamo a suma"
    resultado=suma("cad ",'hola')
    print resultado

    #Para introducir datos por pantalla, raw_input
    nombre=raw_input("Escribe nombre loteria: ")
    print "Nombre introducido: ",nombre

if __name__ == "__main__":
	main()
