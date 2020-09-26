import time
import pandas as pd
import numpy as np

with open('libros_24_meses.txt') as f:
    periodo24_ventas_libros = f.read().split('\n')
    
with open('catalogo_libros.txt') as f:
    catalogo_libros = f.read().split('\n')


inicio = time.time()
libros_vendidos = []

#Se comparan los 2 archivos de texto
coincidencias = set(catalogo_libros).intersection(periodo24_ventas_libros)

for libro in coincidencias:
    libros_vendidos.append(libro)
        

print(len(libros_vendidos))
print('Duracion: {} segundos'.format(time.time() - inicio))