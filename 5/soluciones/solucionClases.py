from coche import coche
from moto import moto
from camion import camion
import random as random

diccionarioVehiculos={}
diccionarioMarcasCoche={1:'Ford',2:'VW',3:'Renault',4:'Fiat',5:'Peugeot'}
diccionarioMarcasMoto={1:'Harley-Davison',2:'Yamaha',3:'BMW',4:'Aprilia'}
diccionarioMarcasCamion={1:'Volvo',2:'Mercedes',3:'Scania',4:'Iveco'}

def main():
    
	for j in range(1,10):
		if j<4:
			nombre='coche'+str(j)
			numero=random.randint(1,5)
			marca=diccionarioMarcasCoche[numero]
			cocheAux=coche(marca)
			diccionarioVehiculos.update({nombre:cocheAux})
		elif j<7:
			nombre='moto'+str(j-3)
			numero=random.randint(1,4)
			marca=diccionarioMarcasMoto[numero]
			motoAux=moto(marca)
			diccionarioVehiculos.update({nombre:motoAux})
		elif j<10:
			nombre='camion'+str(j-6)
			numero=random.randint(1,4)
			marca=diccionarioMarcasCamion[numero]
			camionAux=camion(marca)
			diccionarioVehiculos.update({nombre:camionAux})
	
	print diccionarioVehiculos
	for key, value in diccionarioVehiculos.iteritems():
		print key
		print'---------'
		value.arranca()
		value.circula()
		print ' '
	
	while(True):
		
		for key,value in diccionarioVehiculos.iteritems():
			tiempoCirculando=value.calculaTiempoCirculando()
			
			if tiempoCirculando>3:
				print value.marca
				print'---------'
				value.apagar()
				print ' '
				
		count=0
		for key,value in diccionarioVehiculos.iteritems():
			if value.arrancado==False:
				count=count+1
		if count == 9:
			break
	print 'Todos los vehiculos apagados.'
		
if __name__=='__main__':
    main()
            
