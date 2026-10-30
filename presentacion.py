"""Presentación: todo lo que se muestra por pantalla.

Las tablas se arman con f-strings de ancho fijo para que las columnas
queden alineadas (texto a la izquierda con <, números a la derecha con >).
"""

from campos import PEL_CODIGO, PEL_TITULO, PEL_GENERO, PEL_DURACION
from campos import PEL_CALIFICACION, VIS_NUMERO, VIS_MINUTOS
from campos import CRU_NUMERO, CRU_CODIGO, CRU_TITULO, CRU_GENERO
from campos import CRU_DURACION, CRU_MINUTOS
import estadisticas


def texto_visualizaciones(cantidad):
    """Devuelve '1 visualizacion' o 'N visualizaciones'."""
    if cantidad == 1:
        texto = "1 visualizacion"
    else:
        texto = f"{cantidad} visualizaciones"
    return texto


# ----------------------------------------------------------------------
# Menú
# ----------------------------------------------------------------------
def mostrar_menu():
    print()
    print("=" * 50)
    print("   CATALOGO DE PELICULAS Y VISUALIZACIONES")
    print("=" * 50)
    print(" 1. Listado de películas")
    print(" 2. Consulta de película por código")
    print(" 3. Alta de película")
    print(" 4. Modificación de película")
    print(" 5. Baja de película (en cascada)")
    print(" 6. Listado cruzado de visualizaciones")
    print(" 7. Consulta de visualizaciones por película")
    print(" 8. Estadísticas")
    print(" 9. Generar informe consolidado")
    print(" 0. Salir")
    print("=" * 50)


# ----------------------------------------------------------------------
# Películas
# ----------------------------------------------------------------------
def mostrar_listado_peliculas(peliculas):
    if len(peliculas) == 0:
        print("\nNo hay películas registradas.")
    else:
        print()
        print(f'{"CODIGO":<8}{"TITULO":<25}{"GENERO":<18}{"DURACION":>9}{"CALIF.":>8}')
        print("-" * 68)
        for pelicula in peliculas:
            print(
                f'{pelicula[PEL_CODIGO]:<8}{pelicula[PEL_TITULO]:<25}'
                f'{pelicula[PEL_GENERO]:<18}{pelicula[PEL_DURACION]:>9}'
                f'{pelicula[PEL_CALIFICACION]:>8}'
            )
        print(f"\nTotal: {len(peliculas)} películas.")


def mostrar_pelicula(pelicula):
    print(f"\nPelicula: {pelicula[PEL_TITULO]}")
    print(f"Genero: {pelicula[PEL_GENERO]}")
    print(f"Duracion: {pelicula[PEL_DURACION]} minutos")
    print(f"Calificacion: {pelicula[PEL_CALIFICACION]}")


# ----------------------------------------------------------------------
# Visualizaciones
# ----------------------------------------------------------------------
def mostrar_listado_cruzado(filas):
    if len(filas) == 0:
        print("\nNo hay visualizaciones registradas.")
    else:
        print()
        print(
            f'{"NRO.":<6}{"CODIGO":<8}{"PELICULA":<25}{"GENERO":<18}'
            f'{"DURACION":>9}{"MINUTOS":>9}'
        )
        print("-" * 75)
        for fila in filas:
            print(
                f'{fila[CRU_NUMERO]:<6}{fila[CRU_CODIGO]:<8}'
                f'{fila[CRU_TITULO]:<25}{fila[CRU_GENERO]:<18}'
                f'{fila[CRU_DURACION]:>9}{fila[CRU_MINUTOS]:>9}'
            )
        print(f"\nTotal: {len(filas)} visualizaciones.")


def mostrar_operaciones_pelicula(codigo, pelicula, operaciones, total_minutos):
    print(f"\nCodigo consultado: {codigo}")
    mostrar_pelicula(pelicula)
    if len(operaciones) == 0:
        print("\nLa película no tiene visualizaciones registradas.")
    else:
        print()
        print(f'{"NRO. VISUALIZACION":<20}{"MINUTOS VISTOS":>16}')
        print("-" * 36)
        for operacion in operaciones:
            print(f'{operacion[VIS_NUMERO]:<20}{operacion[VIS_MINUTOS]:>16}')
        print("-" * 36)
        print(f"Operaciones: {len(operaciones)}")
        print(f"Minutos acumulados: {total_minutos}")


# ----------------------------------------------------------------------
# Estadísticas
# ----------------------------------------------------------------------
def mostrar_total_visualizaciones(total):
    print(f"\nCantidad total de visualizaciones: {total}")


def mostrar_visualizaciones_por_pelicula(conteos):
    print("\nVisualizaciones por pelicula:\n")
    for fila in conteos:
        print(
            f"{fila[estadisticas.CONT_CODIGO]} "
            f"{fila[estadisticas.CONT_TITULO]}: "
            f"{fila[estadisticas.CONT_CANTIDAD]}"
        )


def mostrar_mas_visualizadas(mas_vistas):
    print("\nPeliculas mas visualizadas:")
    if len(mas_vistas) == 0:
        print("Todavía no hay visualizaciones registradas.")
    else:
        for fila in mas_vistas:
            cantidad = texto_visualizaciones(fila[estadisticas.CONT_CANTIDAD])
            print(
                f"{fila[estadisticas.CONT_CODIGO]} - "
                f"{fila[estadisticas.CONT_TITULO]} ({cantidad})"
            )


def mostrar_promedio(codigo, titulo, total_minutos, cantidad, promedio):
    if promedio == None:
        print(
            f"\nLa película {codigo} ({titulo}) no tiene visualizaciones: "
            "no es posible calcular el promedio."
        )
    else:
        print(
            f"\nPromedio para {codigo}: {total_minutos} / {cantidad} "
            f"= {promedio:.2f} minutos"
        )
