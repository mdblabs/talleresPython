#!/usr/bin/python

"""
	Programa que genera numeros aleatorios para loterias
	Por mdb.
"""
import random as rand

def generaNumero(loteria):
	
	if (loteria=='Euromillones') | (loteria=='euromillones'):
		print 'Generando boleto de Euromillones...'
		listaNumeros=[]
		listaEstrellas=[]
		numNumeros=0
		numEstrellas=0
		
		while(numNumeros<5):
			numero = rand.randint(1,50)
			if listaNumeros.count(numero)==0:
				listaNumeros.append(numero)
				numNumeros=numNumeros+1
				
		while(numEstrellas<2):
			estrella = rand.randint(1,11)
			if listaEstrellas.count(estrella)==0:
				listaEstrellas.append(estrella)
				numEstrellas=numEstrellas+1
				
		print 'Numeros y Estrellas'
		numEstrellas=0
		for numero in listaNumeros:
			if numEstrellas<2:
				print str(numero)+'	  '+ str(listaEstrellas[numEstrellas])
				numEstrellas = numEstrellas+1
			else:
				print numero
	
	elif (loteria=='Primitiva') | (loteria=='primitiva'):
		print 'Generando boleto Primitiva...'
		listaNumeros=[]
		numNumeros=0
		
		while(numNumeros<6):
			numero = rand.randint(1,49)
			if listaNumeros.count(numero)==0:
				listaNumeros.append(numero)
				numNumeros=numNumeros+1
		
		print"Apuesta sencilla"
		for numero in listaNumeros:
			print numero
		

def main():
	boleto = 'primitiva'
	generaNumero(boleto)

if __name__ == "__main__":
	main()