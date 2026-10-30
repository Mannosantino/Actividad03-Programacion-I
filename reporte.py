"""Construcción del texto del informe consolidado.

Solo arma el texto; guardarlo en el archivo es tarea de archivos.py.
"""

import consultas
import estadisticas
import presentacion
from campos import PEL_CODIGO, PEL_TITULO, PEL_GENERO, PEL_DURACION
from campos import PEL_CALIFICACION, VIS_NUMERO, VIS_MINUTOS

LINEA_DOBLE = "=" * 65
LINEA_SIMPLE = "-" * 65


def armar_bloque_pelicula(pelicula, operaciones):
    """Devuelve las líneas del bloque de una película."""
    total = consultas.total_minutos(operaciones)
    lineas = []
    lineas.append(f"PELICULA: {pelicula[PEL_CODIGO]} - {pelicula[PEL_TITULO]}")
    lineas.append(f"GENERO: {pelicula[PEL_GENERO]}")
    lineas.append(
        f"DURACION: {pelicula[PEL_DURACION]} minutos | "
        f"CALIFICACION: {pelicula[PEL_CALIFICACION]}"
    )
    lineas.append("")
    if len(operaciones) == 0:
        lineas.append("Sin visualizaciones registradas.")
    else:
        lineas.append(f'{"VISUALIZACION":<30}{"MINUTOS VISTOS":>14}')
        lineas.append(LINEA_SIMPLE)
        for operacion in operaciones:
            lineas.append(f"{operacion[VIS_NUMERO]:<30}{operacion[VIS_MINUTOS]:>14}")
    lineas.append("")
    lineas.append(f"OPERACIONES: {len(operaciones)}")
    lineas.append(f"MINUTOS ACUMULADOS: {total}")
    lineas.append("")
    lineas.append("")
    return lineas


def generar_reporte(peliculas, visualizaciones):
    """Devuelve el informe completo como un único texto."""
    lineas = []
    lineas.append(LINEA_DOBLE)
    lineas.append(f'{"INFORME CONSOLIDADO DE VISUALIZACIONES":^65}')
    lineas.append(LINEA_DOBLE)
    lineas.append("")

    for pelicula in peliculas:
        operaciones = consultas.obtener_visualizaciones(
            visualizaciones, pelicula[PEL_CODIGO]
        )
        bloque = armar_bloque_pelicula(pelicula, operaciones)
        for linea in bloque:
            lineas.append(linea)

    conteos = estadisticas.visualizaciones_por_pelicula(peliculas, visualizaciones)
    mas_vistas = estadisticas.peliculas_mas_visualizadas(conteos)

    lineas.append(LINEA_DOBLE)
    lineas.append(f'{"RESUMEN GENERAL":^65}')
    lineas.append(LINEA_DOBLE)
    lineas.append("")
    lineas.append(f"PELICULAS: {len(peliculas)}")
    lineas.append(
        f"VISUALIZACIONES REGISTRADAS: "
        f"{estadisticas.cantidad_total_visualizaciones(visualizaciones)}"
    )
    lineas.append(
        f"MINUTOS VISTOS ACUMULADOS: {consultas.total_minutos(visualizaciones)}"
    )
    lineas.append("")
    lineas.append("PELICULAS MAS VISUALIZADAS:")
    if len(mas_vistas) == 0:
        lineas.append("Sin visualizaciones registradas.")
    for fila in mas_vistas:
        cantidad = presentacion.texto_visualizaciones(fila[estadisticas.CONT_CANTIDAD])
        lineas.append(
            f"{fila[estadisticas.CONT_CODIGO]} - "
            f"{fila[estadisticas.CONT_TITULO]} ({cantidad})"
        )
    lineas.append("")
    lineas.append(LINEA_DOBLE)

    return "\n".join(lineas) + "\n"
