### Equivalente a validate_qty y validate_price ###

def validar_cantidad(cantidad: int) -> bool:
    """Valida que la cantidad sea un entero positivo.

    Args:
        cantidad (int): Cantidad del producto.

    Returns:
        bool: True si la cantidad es válida, False en caso contrario.

    Raises:
        TypeError: Si cantidad no es un entero.

    Example:
        >>> validar_cantidad(5)
        True
        >>> validar_cantidad(0)
        False
        >>> validar_cantidad(-3)
        False
    """
    if cantidad <= 0:
        raise ValueError("cantidad debe ser mayor que 0")
    return True


def validar_precio(precio: float) -> bool:
    """Valida que el precio sea un número no negativo.

    Args:
        precio (float): Precio del producto.

    Returns:
        bool: True si el precio es válido, False en caso contrario.

    Raises:
        TypeError: Si precio no es numérico.

    Example:
        >>> validar_precio(10.5)
        True
        >>> validar_precio(-1)
        False
    """
    if precio <= 0:
        raise ValueError("precio debe ser mayor que 0")
    return True