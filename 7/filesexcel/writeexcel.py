from xlwt import Workbook

#Se crea un 'libro excel' y luego las hojas
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
sheet2 = book.add_sheet('Sheet 2')

#En cada hoja, se seleccionan filas, columnas, dando valor

#Fila,columna,valor
sheet1.write(0,0,'lo que sea')
sheet1.write(0,1,'hola')
sheet1.write(0,2,888)

#Una vez elegido solo una fila, se indica solo la columna en el write
row1 = sheet1.row(1)
row1.write(0,'A2')
row1.write(1,'B2')

#Guardar
book.save('simplewrite.xls')

print 'simplewrite.xls created!'
