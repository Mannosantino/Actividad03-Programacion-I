"""Acceso a archivos de texto.

Es el único módulo que abre, lee y escribe archivos. El resto del
programa trabaja con listas y no sabe cómo se guardan los datos.

Las funciones de este módulo NO capturan errores de archivo: dejan
que FileNotFoundError, OSError o ValueError lleguen a quien las llama
(módulo opciones), que es quien decide qué mensaje mostrar al usuario.
"""

from campos import PEL_CODIGO, PEL_TITULO, PEL_GENERO, PEL_DURACION
from campos import PEL_CALIFICACION, VIS_NUMERO, VIS_CODIGO, VIS_MINUTOS

RUTA_PELICULAS = "peliculas.txt"
RUTA_VISUALIZACIONES = "visualizaciones.txt"
RUTA_REPORTE = "reporte_visualizaciones.txt"
CODIFICACION = "utf-8"
DELIMITADOR = ";"


# ----------------------------------------------------------------------
# Funciones genéricas de lectura y escritura de líneas
# ----------------------------------------------------------------------
def leer_lineas(ruta):
    """Devuelve la lista de líneas del archivo, sin el salto de línea."""
    lineas = []
    archivo = open(ruta, "r", encoding=CODIFICACION)
    try:
        for linea in archivo:
            lineas.append(linea.strip())
    finally:
        archivo.close()
    return lineas


def escribir_lineas(ruta, lineas):
    """Crea (o sobrescribe) el archivo con una línea por elemento."""
    archivo = open(ruta, "w", encoding=CODIFICACION)
    try:
        for linea in lineas:
            archivo.write(linea + "\n")
    finally:
        archivo.close()


# ----------------------------------------------------------------------
# peliculas.txt
# ----------------------------------------------------------------------
def convertir_linea_pelicula(linea, numero_linea):
    """Convierte una línea de texto en un registro de película.

    Lanza ValueError si la línea no tiene 5 campos o si un campo
    numérico no se puede convertir.
    """
    partes = linea.split(DELIMITADOR)
    if len(partes) != 5:
        raise ValueError(
            f"línea {numero_linea}: se esperaban 5 campos y hay {len(partes)}."
        )
    try:
        codigo = int(partes[0])
        duracion = int(partes[3])
        calificacion = int(partes[4])
    except ValueError:
        raise ValueError(f"línea {numero_linea}: hay un campo numérico inválido.")
    return [codigo, partes[1].strip(), partes[2].strip(), duracion, calificacion]


def formatear_pelicula(pelicula):
    """Convierte un registro de película en la línea de texto a guardar."""
    d = DELIMITADOR
    return (
        f"{pelicula[PEL_CODIGO]}{d}{pelicula[PEL_TITULO]}{d}"
        f"{pelicula[PEL_GENERO]}{d}{pelicula[PEL_DURACION]}{d}"
        f"{pelicula[PEL_CALIFICACION]}"
    )


def leer_peliculas():
    """Lee peliculas.txt y devuelve una lista de registros (matriz)."""
    peliculas = []
    numero_linea = 0
    for linea in leer_lineas(RUTA_PELICULAS):
        numero_linea += 1
        if linea != "":
            peliculas.append(convertir_linea_pelicula(linea, numero_linea))
    return peliculas


def guardar_peliculas(peliculas):
    """Reescribe peliculas.txt completo con la lista recibida."""
    lineas = []
    for pelicula in peliculas:
        lineas.append(formatear_pelicula(pelicula))
    escribir_lineas(RUTA_PELICULAS, lineas)


def agregar_pelicula(pelicula):
    """Agrega un registro al final de peliculas.txt sin perder los anteriores.

    Usa el modo 'a' (append). Supone que el archivo termina en salto de
    línea, algo que siempre cumple lo que escribe este programa.
    """
    archivo = open(RUTA_PELICULAS, "a", encoding=CODIFICACION)
    try:
        archivo.write(formatear_pelicula(pelicula) + "\n")
    finally:
        archivo.close()


# ----------------------------------------------------------------------
# visualizaciones.txt
# ----------------------------------------------------------------------
def convertir_linea_visualizacion(linea, numero_linea):
    """Convierte una línea de texto en un registro de visualización."""
    partes = linea.split(DELIMITADOR)
    if len(partes) != 3:
        raise ValueError(
            f"línea {numero_linea}: se esperaban 3 campos y hay {len(partes)}."
        )
    try:
        numero = int(partes[0])
        codigo = int(partes[1])
        minutos = int(partes[2])
    except ValueError:
        raise ValueError(f"línea {numero_linea}: hay un campo numérico inválido.")
    return [numero, codigo, minutos]


def leer_visualizaciones():
    """Lee visualizaciones.txt y devuelve una lista de registros."""
    visualizaciones = []
    numero_linea = 0
    for linea in leer_lineas(RUTA_VISUALIZACIONES):
        numero_linea += 1
        if linea != "":
            visualizaciones.append(convertir_linea_visualizacion(linea, numero_linea))
    return visualizaciones


def guardar_visualizaciones(visualizaciones):
    """Reescribe visualizaciones.txt completo con la lista recibida."""
    d = DELIMITADOR
    lineas = []
    for visualizacion in visualizaciones:
        lineas.append(
            f"{visualizacion[VIS_NUMERO]}{d}{visualizacion[VIS_CODIGO]}"
            f"{d}{visualizacion[VIS_MINUTOS]}"
        )
    escribir_lineas(RUTA_VISUALIZACIONES, lineas)


# ----------------------------------------------------------------------
# reporte_visualizaciones.txt
# ----------------------------------------------------------------------
def guardar_reporte(texto):
    """Escribe el informe, sobrescribiendo la versión anterior."""
    archivo = open(RUTA_REPORTE, "w", encoding=CODIFICACION)
    try:
        archivo.write(texto)
    finally:
        archivo.close()
