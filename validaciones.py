"""Validaciones de datos.

Las funciones reciben un texto, lo validan y devuelven el valor ya
convertido. Si el dato no es válido, lanzan ValueError con un mensaje
comprensible (raise). No leen datos del teclado ni imprimen nada.
"""

CARACTER_PROHIBIDO = ";"  # es el delimitador de los archivos
MAXIMO_ENTERO = 999999    # tope razonable para códigos y minutos


def validar_entero(texto, nombre, minimo, maximo):
    """Convierte texto a entero y verifica que esté entre minimo y maximo.

    nombre: cómo se llama el dato en los mensajes (ej.: "La duración").
    """
    try:
        numero = int(texto)
    except ValueError:
        raise ValueError(f"{nombre} debe ser un número entero.")
    if numero < minimo:
        raise ValueError(f"{nombre} debe ser mayor o igual a {minimo}.")
    if numero > maximo:
        raise ValueError(f"{nombre} debe ser menor o igual a {maximo}.")
    return numero


def validar_texto(texto, nombre):
    """Verifica que el texto no esté vacío ni contenga el delimitador."""
    texto = texto.strip()
    if texto == "":
        raise ValueError(f"{nombre} no puede estar vacío.")
    if CARACTER_PROHIBIDO in texto:
        raise ValueError(
            f"{nombre} no puede contener el carácter '{CARACTER_PROHIBIDO}'."
        )
    return texto
