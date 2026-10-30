"""Lectura de datos por teclado con validación y reintento.

Cada función repite la pregunta hasta que el usuario ingresa un dato
válido, de modo que un error de tipeo nunca finaliza el programa.
"""

import validaciones


def pedir_entero(mensaje, nombre, minimo, maximo):
    """Pide un entero entre minimo y maximo, reintentando si es inválido."""
    numero = 0
    valido = False
    while not valido:
        texto = input(mensaje)
        try:
            numero = validaciones.validar_entero(texto, nombre, minimo, maximo)
            valido = True
        except ValueError as error:
            print(f"  Error: {error} Intente nuevamente.")
    return numero


def pedir_codigo(mensaje):
    """Pide un código de película (entero positivo)."""
    return pedir_entero(mensaje, "El código", 1, validaciones.MAXIMO_ENTERO)


def pedir_entero_o_actual(mensaje, nombre, minimo, maximo, valor_actual):
    """Igual que pedir_entero, pero Enter sin escribir conserva valor_actual."""
    numero = valor_actual
    valido = False
    while not valido:
        texto = input(mensaje).strip()
        if texto == "":
            valido = True
        else:
            try:
                numero = validaciones.validar_entero(texto, nombre, minimo, maximo)
                valido = True
            except ValueError as error:
                print(f"  Error: {error} Intente nuevamente.")
    return numero


def pedir_texto(mensaje, nombre):
    """Pide un texto no vacío, reintentando si es inválido."""
    resultado = ""
    valido = False
    while not valido:
        texto = input(mensaje)
        try:
            resultado = validaciones.validar_texto(texto, nombre)
            valido = True
        except ValueError as error:
            print(f"  Error: {error} Intente nuevamente.")
    return resultado


def pedir_texto_o_actual(mensaje, nombre, valor_actual):
    """Igual que pedir_texto, pero Enter sin escribir conserva valor_actual."""
    resultado = valor_actual
    valido = False
    while not valido:
        texto = input(mensaje).strip()
        if texto == "":
            valido = True
        else:
            try:
                resultado = validaciones.validar_texto(texto, nombre)
                valido = True
            except ValueError as error:
                print(f"  Error: {error} Intente nuevamente.")
    return resultado


def pedir_confirmacion(mensaje):
    """Pregunta por s/n y devuelve True (sí) o False (no)."""
    confirmado = False
    valido = False
    while not valido:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta == "s":
            confirmado = True
            valido = True
        elif respuesta == "n":
            valido = True
        else:
            print("  Error: responda 's' para confirmar o 'n' para cancelar.")
    return confirmado
