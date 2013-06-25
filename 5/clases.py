""" Clases """

class Coche:
    """Clase coche"""
    def __init__(self,colordelcoche,gasolina):
        self.color=colordelcoche
        self.combustible=gasolina
        self.personas=0
        self.numruedas=4

    def arranca(self):
        if self.combustible == 'diesel':
            print 'este coche arranca con diesel'
        else:
            print 'este coche arranca con gasolina'  

    def transportar(self):
        print "el vehiculo transporta a: " , self.personas, " personas"
    
    pass

class Matrix:
    def __init__(self,row,col):
        self.row=row
        self.col=col

        
    def inversa(self):
        if self.determinante() == 0:
            print 'no se puede...'
   
    def determinante(self):
        #calculo determinante
        # ...
        valordeterminante=0
        print 'fin de calculo'
        
        return valordeterminante  
      
    pass
        
	    

def main():
    print 'Inicio programa'

    #Un coche
    cochePepe=Coche('rojo','diesel')
    cochePepe.combustible='gasolina'
    cochePepe.arranca()

    cochePepe.transportar()
    cochePepe.personas=5
    cochePepe.transportar()

    #Otros coches
    coche1=Coche('verde','gasolina')
    coche2=Coche('azul','diesel')

    coche1.arranca()
    coche1.numruedas=6

    #Objeto de Matrix: mimatriz
    mimatriz=Matrix(2,2)
    mimatriz.inversa()

    

if __name__ == "__main__":
    main()
