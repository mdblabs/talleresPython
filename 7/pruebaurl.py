"""

Interaccion con webs.
Metodos para obtener informacion de una web,
y libreria BeautifulSoup para dar formato
segun las etiqiuetas html

"""


import urllib2 as url
from bs4 import BeautifulSoup

try:
    mipagina=url.urlopen("http://www.google.com")
except:
    print 'No se pudo abrir'

# Mi pagina sin formato
html = mipagina.read()
#print html


# Mi pagina con formato, cogiendo las etiquetas html
soup = BeautifulSoup(html)
print soup.prettify()
