"""Posiciones de cada campo dentro de los registros del sistema.

Cada registro se representa con una lista. En lugar de escribir
pelicula[3] (que no dice nada), se usan nombres como PEL_DURACION.
Son constantes: nunca cambian, por lo que no se consideran variables
globales para compartir datos.
"""

# peliculas.txt -> [codigo, titulo, genero, duracion, calificacion]
PEL_CODIGO = 0
PEL_TITULO = 1
PEL_GENERO = 2
PEL_DURACION = 3
PEL_CALIFICACION = 4

# visualizaciones.txt -> [numero_visualizacion, codigo_pelicula, minutos_vistos]
VIS_NUMERO = 0
VIS_CODIGO = 1
VIS_MINUTOS = 2

# Filas del listado cruzado -> [nro, codigo, titulo, genero, duracion, minutos]
CRU_NUMERO = 0
CRU_CODIGO = 1
CRU_TITULO = 2
CRU_GENERO = 3
CRU_DURACION = 4
CRU_MINUTOS = 5
