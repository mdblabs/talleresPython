class vehiculo:
	def __init__(self,planta,color,carga):
		self.plantaPotencia=planta
		self.colorVehiculo=color
		self.cargaVehiculo=carga
		self.arrancado=False
	
	def arranca():
		self.arrancado=True
	
	def para():
		self.arrancado=False
	
	def imprimete(self):
		print self.plantaPotencia
		print self.colorVehiculo
		print self.cargaVehiculo
	pass
	
class coche(vehiculo):
	
	def __init__(self,planta,color,carga,numPlazas):
		vehiculo.__init__(self,planta,color,carga)
		self.plazas=numPlazas
	
	def imprimete(self):
		print self.plazas
	
	def imprimete(self,marca):
		print self.plazas
		print marca
		
	pass

miVehiculo=vehiculo('diesel','rojo',300)
miCoche=coche('diesel','rojo',300,5)
miVehiculo.imprimete()
miCoche.imprimete('Mercedes')
miCoche.imprimete(3)

		