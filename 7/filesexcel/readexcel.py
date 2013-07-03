from xlrd import open_workbook

#leer el libro excel
wb = open_workbook('simple.xls')

#para cada hoja del libro
for s in wb.sheets():
    print 'Sheet:',s.name
    
    #para cada fila y columna
    for row in range(s.nrows):
        values =[]
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print ' '.join(values)


