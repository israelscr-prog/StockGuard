from stockguard import add_item as add_item_original
from stockguard import update_price as update_price_original
from validator import validar_cantidad, validar_precio


def agregar_item(nombre: str, cantidad: int, precio: float):
    """Añade un producto validando cantidad y precio.

    Args:
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad.
        precio (float): Precio.

    Raises:
        ValueError: Si cantidad o precio no son válidos.
    """
    if not validar_cantidad(cantidad):
        raise ValueError("Cantidad inválida.")

    if not validar_precio(precio):
        raise ValueError("Precio inválido.")

    return add_item_original(nombre, cantidad, precio)


def actualizar_precio(nombre: str, nuevo_precio: float):
    """Actualiza el precio validándolo.

    Args:
        nombre (str): Nombre del producto.
        nuevo_precio (float): Nuevo precio.

    Raises:
        ValueError: Si el precio no es válido.
    """
    if not validar_precio(nuevo_precio):
        raise ValueError("Precio inválido.")

    return update_price_original(nombre, nuevo_precio)