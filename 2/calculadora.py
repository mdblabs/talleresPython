""" Esto es una calculadora simple """
a=3
b=5.

def suma():
	"""Esto es una funcion suma" """
	print a+b

def resta():
	"""Esto es una funcion resta """
	print a-b

def multiplica():
	"""Esto es una funcion multiplica """
	print a*b

def divide():
	"""Esto es una funcion divide """
	print a/b

def main():
        print "valores: ", a, " y ", b
        
        print "suma: "
        suma()
        
        print "resta: "
        resta()
        
        print "multiplica: "
        multiplica()
        
        print "divide: "
        divide()
        

if __name__ == "__main__":
	main()
