"""
#Importa todas los metodos de funciones.py y nombralo "f"
import suma as f

res=f.suma(3,4)
print res
"""

#importa solo el metodo suma de funciones.py
from funciones import suma as f

res=f(3,4)
print res
