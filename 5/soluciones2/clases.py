import time

class Coche:
    """Clase coche"""
    def __init__(self,colordelcoche,gasolina):
        self.color=colordelcoche
        self.combustible=gasolina
        
        self.personas=0
        self.numruedas=4

        self.arrancado=False
        self.circulando=False

    def arranca(self):
        if(self.arrancado==False):
            self.arrancado==True
            print 'arranca coche'

    def parar(self):
        self.arrancado=False
        print 'parar coche'
    
    pass

class Moto:
    """Clase moto"""
    def __init__(self,colordemoto,gasolina):
        self.color=colordemoto
        self.combustible=gasolina
        
        self.personas=0
        self.numruedas=2

        self.arrancado=False
        self.circulando=False

    def arranca(self):
        if(self.arrancado==False):
            self.arrancado==True
            print 'arranca moto'

    def parar(self):
        self.arrancado=False
        print 'parar moto'
    
    pass


class Camion:
    """Clase moto"""
    def __init__(self,color,tipogasolina):
        self.color=color
        self.combustible=tipogasolina
        
        self.personas=0
        self.numruedas=2

        self.trailer=True

        self.arrancado=False
        self.circulando=False

    def arranca(self):
        if(self.arrancado==False):
            self.arrancado==True
            print 'arranca camion'

    def parar(self):
        self.arrancado=False
        print 'parar camion'
    
    pass


def main():

    micoche=Coche('rojo','gasolina')
    micoche.arranca()

    mimoto=Moto('azul','gasolina')
    mimoto.arranca()

    micamionmola=Camion('amarillo','gasolina')
    micamionmola.arranca()
    
    print 'vehiculos circulando...'
    time.sleep(2)
    
    micoche.parar()
    mimoto.parar()
    micamionmola.parar()
    

if __name__ == "__main__":
    main()
