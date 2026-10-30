"""Una función por cada opción del menú.

Cada función coordina los demás módulos: carga datos, pide información
al usuario, llama a consultas / gestión / estadísticas, guarda y muestra.
Es el lugar donde se capturan las excepciones de archivos y de búsqueda.

Los datos se leen desde el archivo en cada operación, así que los
archivos son siempre la fuente principal de información y no hacen
falta variables globales.
"""

import archivos
import consultas
import entrada
import estadisticas
import gestion
import presentacion
import reporte
import validaciones
from campos import PEL_CODIGO, PEL_TITULO, PEL_GENERO, PEL_DURACION
from campos import PEL_CALIFICACION


# ----------------------------------------------------------------------
# Carga de datos con manejo de errores
# ----------------------------------------------------------------------
def cargar_peliculas():
    """Lee peliculas.txt. Devuelve la lista, o None si hubo un error."""
    peliculas = None
    try:
        peliculas = archivos.leer_peliculas()
    except FileNotFoundError:
        print(
            f"\nError: no se encontró el archivo '{archivos.RUTA_PELICULAS}'. "
            "Verifique que esté en la carpeta del programa."
        )
    except ValueError as error:
        print(f"\nError en los datos de '{archivos.RUTA_PELICULAS}': {error}")
    except OSError as error:
        print(f"\nError al leer '{archivos.RUTA_PELICULAS}': {error}")
    return peliculas


def cargar_visualizaciones():
    """Lee visualizaciones.txt. Devuelve la lista, o None si hubo un error."""
    visualizaciones = None
    try:
        visualizaciones = archivos.leer_visualizaciones()
    except FileNotFoundError:
        print(
            f"\nError: no se encontró el archivo '{archivos.RUTA_VISUALIZACIONES}'. "
            "Verifique que esté en la carpeta del programa."
        )
    except ValueError as error:
        print(f"\nError en los datos de '{archivos.RUTA_VISUALIZACIONES}': {error}")
    except OSError as error:
        print(f"\nError al leer '{archivos.RUTA_VISUALIZACIONES}': {error}")
    return visualizaciones


def cargar_datos():
    """Lee ambos archivos. Devuelve [peliculas, visualizaciones] o None."""
    datos = None
    peliculas = cargar_peliculas()
    if peliculas != None:
        visualizaciones = cargar_visualizaciones()
        if visualizaciones != None:
            datos = [peliculas, visualizaciones]
    return datos


def pedir_pelicula_existente(peliculas):
    """Pide un código y busca la película.

    Devuelve la posición en la lista, o NO_ENCONTRADO (-1) si no existe.
    La excepción ValueError que lanza la búsqueda se maneja acá.
    """
    indice = consultas.NO_ENCONTRADO
    codigo = entrada.pedir_codigo("Código de la película: ")
    try:
        indice = consultas.buscar_pelicula(peliculas, codigo)
    except ValueError as error:
        print(f"\n{error}")
    return indice


# ----------------------------------------------------------------------
# 1. Listado
# ----------------------------------------------------------------------
def opcion_listar():
    peliculas = cargar_peliculas()
    if peliculas != None:
        presentacion.mostrar_listado_peliculas(peliculas)


# ----------------------------------------------------------------------
# 2. Consulta por código
# ----------------------------------------------------------------------
def opcion_consultar():
    peliculas = cargar_peliculas()
    if peliculas != None:
        indice = pedir_pelicula_existente(peliculas)
        if indice != consultas.NO_ENCONTRADO:
            pelicula = peliculas[indice]
            print(f"\nCodigo: {pelicula[PEL_CODIGO]}", end="")
            presentacion.mostrar_pelicula(pelicula)


# ----------------------------------------------------------------------
# 3. Alta
# ----------------------------------------------------------------------
def pedir_y_guardar_alta(peliculas):
    """Pide los campos de la película nueva y la agrega al archivo."""
    codigo = entrada.pedir_codigo("Código nuevo: ")
    if consultas.codigo_existe(peliculas, codigo):
        print(f"\nAlta rechazada: ya existe una película con código {codigo}.")
    else:
        titulo = entrada.pedir_texto("Título: ", "El título")
        genero = entrada.pedir_texto("Género: ", "El género")
        duracion = entrada.pedir_entero(
            "Duración (minutos): ", "La duración", 1, validaciones.MAXIMO_ENTERO
        )
        calificacion = entrada.pedir_entero(
            "Calificación (1 a 5): ", "La calificación", 1, 5
        )
        nueva = gestion.crear_pelicula(codigo, titulo, genero, duracion, calificacion)
        try:
            archivos.agregar_pelicula(nueva)
        except OSError as error:
            print(f"\nError: no se pudo guardar la película: {error}")
        else:
            print(f"\nPelícula {codigo} - {titulo} agregada correctamente.")


def opcion_alta():
    peliculas = cargar_peliculas()
    if peliculas != None:
        pedir_y_guardar_alta(peliculas)


# ----------------------------------------------------------------------
# 4. Modificación
# ----------------------------------------------------------------------
def pedir_y_guardar_modificacion(peliculas, indice):
    """Pide los nuevos valores (Enter conserva el actual) y guarda."""
    actual = peliculas[indice]
    print("\nDatos actuales:", end="")
    presentacion.mostrar_pelicula(actual)
    print("\nPresione Enter sin escribir nada para mantener el valor actual.")

    titulo = entrada.pedir_texto_o_actual(
        f"Título [{actual[PEL_TITULO]}]: ", "El título", actual[PEL_TITULO]
    )
    genero = entrada.pedir_texto_o_actual(
        f"Género [{actual[PEL_GENERO]}]: ", "El género", actual[PEL_GENERO]
    )
    duracion = entrada.pedir_entero_o_actual(
        f"Duración [{actual[PEL_DURACION]}]: ", "La duración",
        1, validaciones.MAXIMO_ENTERO, actual[PEL_DURACION]
    )
    calificacion = entrada.pedir_entero_o_actual(
        f"Calificación [{actual[PEL_CALIFICACION]}]: ", "La calificación",
        1, 5, actual[PEL_CALIFICACION]
    )

    gestion.modificar_pelicula(peliculas, indice, titulo, genero, duracion, calificacion)
    try:
        archivos.guardar_peliculas(peliculas)
    except OSError as error:
        print(f"\nError: no se pudieron guardar los cambios: {error}")
    else:
        print("\nPelícula modificada correctamente.")


def opcion_modificar():
    peliculas = cargar_peliculas()
    if peliculas != None:
        indice = pedir_pelicula_existente(peliculas)
        if indice != consultas.NO_ENCONTRADO:
            pedir_y_guardar_modificacion(peliculas, indice)


# ----------------------------------------------------------------------
# 5. Baja en cascada
# ----------------------------------------------------------------------
def eliminar_en_cascada(peliculas, visualizaciones, codigo, cantidad):
    """Elimina la película y sus visualizaciones, y guarda ambos archivos."""
    peliculas_restantes = gestion.eliminar_pelicula(peliculas, codigo)
    visualizaciones_restantes = gestion.eliminar_visualizaciones_de(
        visualizaciones, codigo
    )
    try:
        # Se guardan primero las visualizaciones: si algo fallara a mitad
        # de camino, nunca quedarían visualizaciones de una película
        # inexistente (dato inconsistente).
        if cantidad > 0:
            archivos.guardar_visualizaciones(visualizaciones_restantes)
        archivos.guardar_peliculas(peliculas_restantes)
    except OSError as error:
        print(f"\nError: no se pudo completar la baja: {error}")
    else:
        print(
            f"\nPelícula {codigo} eliminada junto con {cantidad} "
            "visualización(es) relacionada(s)."
        )


def confirmar_baja(peliculas, visualizaciones, indice):
    """Muestra la película, cuenta sus visualizaciones y pide confirmación."""
    pelicula = peliculas[indice]
    codigo = pelicula[PEL_CODIGO]
    cantidad = consultas.contar_visualizaciones(visualizaciones, codigo)

    print(f"\nCodigo: {codigo}", end="")
    presentacion.mostrar_pelicula(pelicula)
    print(f"\nVisualizaciones relacionadas que también se eliminarán: {cantidad}")

    if entrada.pedir_confirmacion("¿Confirma la baja?"):
        eliminar_en_cascada(peliculas, visualizaciones, codigo, cantidad)
    else:
        print("\nBaja cancelada. No se modificó ningún archivo.")


def opcion_baja():
    datos = cargar_datos()
    if datos != None:
        peliculas = datos[0]
        visualizaciones = datos[1]
        indice = pedir_pelicula_existente(peliculas)
        if indice != consultas.NO_ENCONTRADO:
            confirmar_baja(peliculas, visualizaciones, indice)


# ----------------------------------------------------------------------
# 6. Listado cruzado
# ----------------------------------------------------------------------
def opcion_listado_cruzado():
    datos = cargar_datos()
    if datos != None:
        filas = consultas.cruzar_operaciones(datos[0], datos[1])
        presentacion.mostrar_listado_cruzado(filas)


# ----------------------------------------------------------------------
# 7. Consulta de visualizaciones por película
# ----------------------------------------------------------------------
def opcion_operaciones_por_codigo():
    datos = cargar_datos()
    if datos != None:
        peliculas = datos[0]
        visualizaciones = datos[1]
        indice = pedir_pelicula_existente(peliculas)
        if indice != consultas.NO_ENCONTRADO:
            pelicula = peliculas[indice]
            codigo = pelicula[PEL_CODIGO]
            operaciones = consultas.obtener_visualizaciones(visualizaciones, codigo)
            total = consultas.total_minutos(operaciones)
            presentacion.mostrar_operaciones_pelicula(
                codigo, pelicula, operaciones, total
            )


# ----------------------------------------------------------------------
# 8. Estadísticas
# ----------------------------------------------------------------------
def mostrar_promedio_de_pelicula(peliculas, visualizaciones, indice):
    """Estadística 4 para la película elegida."""
    pelicula = peliculas[indice]
    operaciones = consultas.obtener_visualizaciones(
        visualizaciones, pelicula[PEL_CODIGO]
    )
    total_minutos = consultas.total_minutos(operaciones)
    promedio = estadisticas.promedio_minutos(total_minutos, len(operaciones))
    presentacion.mostrar_promedio(
        pelicula[PEL_CODIGO], pelicula[PEL_TITULO],
        total_minutos, len(operaciones), promedio
    )


def opcion_estadisticas():
    datos = cargar_datos()
    if datos != None:
        peliculas = datos[0]
        visualizaciones = datos[1]

        total = estadisticas.cantidad_total_visualizaciones(visualizaciones)
        conteos = estadisticas.visualizaciones_por_pelicula(peliculas, visualizaciones)
        mas_vistas = estadisticas.peliculas_mas_visualizadas(conteos)

        presentacion.mostrar_total_visualizaciones(total)
        presentacion.mostrar_visualizaciones_por_pelicula(conteos)
        presentacion.mostrar_mas_visualizadas(mas_vistas)

        print("\nPromedio de minutos vistos por visualización:")
        indice = pedir_pelicula_existente(peliculas)
        if indice != consultas.NO_ENCONTRADO:
            mostrar_promedio_de_pelicula(peliculas, visualizaciones, indice)


# ----------------------------------------------------------------------
# 9. Informe consolidado
# ----------------------------------------------------------------------
def opcion_reporte():
    datos = cargar_datos()
    if datos != None:
        texto = reporte.generar_reporte(datos[0], datos[1])
        try:
            archivos.guardar_reporte(texto)
        except OSError as error:
            print(f"\nError: no se pudo generar el informe: {error}")
        else:
            print(f"\nInforme generado correctamente en '{archivos.RUTA_REPORTE}'.")
