"""Operaciones de alta, modificación y baja sobre las listas en memoria.

Solo transforman listas. Guardar los cambios en los archivos es
responsabilidad del módulo archivos (invocado desde opciones).
"""

from campos import PEL_CODIGO, PEL_TITULO, PEL_GENERO, PEL_DURACION
from campos import PEL_CALIFICACION, VIS_CODIGO


def crear_pelicula(codigo, titulo, genero, duracion, calificacion):
    """Arma un registro de película con el orden de campos del archivo."""
    return [codigo, titulo, genero, duracion, calificacion]


def modificar_pelicula(peliculas, indice, titulo, genero, duracion, calificacion):
    """Cambia todos los campos de la película, excepto el código."""
    peliculas[indice][PEL_TITULO] = titulo
    peliculas[indice][PEL_GENERO] = genero
    peliculas[indice][PEL_DURACION] = duracion
    peliculas[indice][PEL_CALIFICACION] = calificacion


def eliminar_pelicula(peliculas, codigo):
    """Devuelve una lista nueva sin la película indicada."""
    restantes = []
    for pelicula in peliculas:
        if pelicula[PEL_CODIGO] != codigo:
            restantes.append(pelicula)
    return restantes


def eliminar_visualizaciones_de(visualizaciones, codigo):
    """Devuelve una lista nueva sin las visualizaciones de esa película."""
    restantes = []
    for visualizacion in visualizaciones:
        if visualizacion[VIS_CODIGO] != codigo:
            restantes.append(visualizacion)
    return restantes
