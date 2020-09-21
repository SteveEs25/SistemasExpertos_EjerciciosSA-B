import time
import pandas as pd
import numpy as np


with open('libros_24_meses.txt') as f:
    periodo24_ventas_libros = f.read().split('\n')
    
with open('catalogo_libros.txt') as f:
    catalogo_libros = f.read().split('\n')

with open('costos.txt') as costos:
    costos = costos.read().split('\n')



inicio = time.time()
seleccion = np.array(costos, int)

inversion = np.sum(seleccion, where = (seleccion <= 25))
    	
        

print('El monto total a invertir es de: $ ' + str(inversion))
print('Duracion: {} segundos'.format(time.time() - inicio))