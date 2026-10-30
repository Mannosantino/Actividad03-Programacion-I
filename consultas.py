"""Búsquedas y cruces de datos sobre las listas en memoria.

No leen archivos, no piden datos y no imprimen: solo reciben listas
por parámetro y devuelven resultados.
"""

from campos import PEL_CODIGO, PEL_TITULO, PEL_GENERO, PEL_DURACION
from campos import VIS_NUMERO, VIS_CODIGO, VIS_MINUTOS

NO_ENCONTRADO = -1


def buscar_pelicula(peliculas, codigo):
    """Búsqueda secuencial. Devuelve la posición de la película.

    Si el código no existe, lanza ValueError (raise). Quien llama a esta
    función es quien maneja la excepción.
    """
    fila = 0
    encontrado = False
    while fila < len(peliculas) and not encontrado:
        if peliculas[fila][PEL_CODIGO] == codigo:
            encontrado = True
        else:
            fila += 1
    if not encontrado:
        raise ValueError(f"No existe una película con código {codigo}.")
    return fila


def codigo_existe(peliculas, codigo):
    """Devuelve True si ya hay una película con ese código."""
    try:
        buscar_pelicula(peliculas, codigo)
        existe = True
    except ValueError:
        existe = False
    return existe


def obtener_visualizaciones(visualizaciones, codigo):
    """Devuelve solo las visualizaciones de la película indicada."""
    encontradas = []
    for visualizacion in visualizaciones:
        if visualizacion[VIS_CODIGO] == codigo:
            encontradas.append(visualizacion)
    return encontradas


def contar_visualizaciones(visualizaciones, codigo):
    """Devuelve cuántas visualizaciones tiene una película."""
    cantidad = 0
    for visualizacion in visualizaciones:
        if visualizacion[VIS_CODIGO] == codigo:
            cantidad += 1
    return cantidad


def total_minutos(visualizaciones):
    """Suma los minutos vistos de la lista de visualizaciones recibida."""
    total = 0
    for visualizacion in visualizaciones:
        total += visualizacion[VIS_MINUTOS]
    return total


def cruzar_operaciones(peliculas, visualizaciones):
    """Une cada visualización con los datos de su película (por código).

    Devuelve filas: [nro, codigo, titulo, genero, duracion, minutos].
    Si el código no existiera en peliculas.txt (dato inconsistente),
    la fila se genera igual con la película marcada como no encontrada.
    """
    filas = []
    for visualizacion in visualizaciones:
        try:
            indice = buscar_pelicula(peliculas, visualizacion[VIS_CODIGO])
            titulo = peliculas[indice][PEL_TITULO]
            genero = peliculas[indice][PEL_GENERO]
            duracion = peliculas[indice][PEL_DURACION]
        except ValueError:
            titulo = "(no encontrada)"
            genero = "-"
            duracion = "-"
        filas.append([
            visualizacion[VIS_NUMERO],
            visualizacion[VIS_CODIGO],
            titulo,
            genero,
            duracion,
            visualizacion[VIS_MINUTOS],
        ])
    return filas
