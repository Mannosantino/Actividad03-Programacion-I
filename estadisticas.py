"""Estadísticas requeridas. Una función por responsabilidad.

Solo calculan y devuelven resultados; no imprimen ni leen archivos.
"""

import consultas
from campos import PEL_CODIGO, PEL_TITULO

# Posiciones de cada fila devuelta por visualizaciones_por_pelicula()
CONT_CODIGO = 0
CONT_TITULO = 1
CONT_CANTIDAD = 2


def cantidad_total_visualizaciones(visualizaciones):
    """Estadística 1: cantidad total de visualizaciones registradas."""
    return len(visualizaciones)


def visualizaciones_por_pelicula(peliculas, visualizaciones):
    """Estadística 2: filas [codigo, titulo, cantidad], con 0 si no hay."""
    conteos = []
    for pelicula in peliculas:
        cantidad = consultas.contar_visualizaciones(
            visualizaciones, pelicula[PEL_CODIGO]
        )
        conteos.append([pelicula[PEL_CODIGO], pelicula[PEL_TITULO], cantidad])
    return conteos


def peliculas_mas_visualizadas(conteos):
    """Estadística 3: todas las filas empatadas en el máximo.

    Recibe la lista que devuelve visualizaciones_por_pelicula().
    Si no hay ninguna visualización, devuelve una lista vacía.
    """
    maximo = 0
    for fila in conteos:
        if fila[CONT_CANTIDAD] > maximo:
            maximo = fila[CONT_CANTIDAD]

    mas_vistas = []
    if maximo > 0:
        for fila in conteos:
            if fila[CONT_CANTIDAD] == maximo:
                mas_vistas.append(fila)
    return mas_vistas


def promedio_minutos(total_minutos, cantidad):
    """Estadística 4: promedio de minutos vistos por visualización.

    Devuelve None si la película no tiene visualizaciones (en lugar de
    dejar que el ZeroDivisionError finalice el programa).
    """
    try:
        promedio = total_minutos / cantidad
    except ZeroDivisionError:
        promedio = None
    return promedio
