from datetime import datetime

class moto:
	def __init__(self,marca):
		self.marca=marca
		self.arrancado=False
		self.circulando=False
		self.tiempoEnCirculacion=0
		self.tiempoCirculando=0
	
	def arranca(self):
		if self.arrancado==False:
			print 'Estoy arrancando'
			self.arrancado=True
		else:
			print'Ya estoy arrancado'
	
	def apagar(self):
		self.arrancado=False
		print 'Estoy apagado'
	
	def calculaTiempoCirculando(self):
		self.tiempoCirculando = (datetime.now()-self.tiempoEnCirculacion).total_seconds()
		return self.tiempoCirculando
	
	def circula(self):
		if (self.arrancado==True and self.circulando==False):
			self.tiempoEnCirculacion=datetime.now()
			self.circulando=True
			print 'Circulando!'
		elif self.arrancado==False:
			print 'No estoy arrancado'
		elif self.circulando==True:
			print 'Ya estoy circulando y llevo ' + str(self.calculaTiempoCirculando())+' segundos circulando.'