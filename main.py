"""Programa principal: menú del catálogo de películas.

Ejecutar con:  python main.py   (desde la carpeta que contiene los .txt)
"""

import entrada
import opciones
import presentacion


def main():
    opcion = -1
    while opcion != 0:
        presentacion.mostrar_menu()
        opcion = entrada.pedir_entero("Seleccione una opción: ", "La opción", 0, 9)

        if opcion == 1:
            opciones.opcion_listar()
        elif opcion == 2:
            opciones.opcion_consultar()
        elif opcion == 3:
            opciones.opcion_alta()
        elif opcion == 4:
            opciones.opcion_modificar()
        elif opcion == 5:
            opciones.opcion_baja()
        elif opcion == 6:
            opciones.opcion_listado_cruzado()
        elif opcion == 7:
            opciones.opcion_operaciones_por_codigo()
        elif opcion == 8:
            opciones.opcion_estadisticas()
        elif opcion == 9:
            opciones.opcion_reporte()
        else:
            print("\nPrograma finalizado. ¡Hasta luego!")


main()
