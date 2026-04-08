import json
import os

ARCHIVO_INVENTARIO = "inventory.json"


def cargar_inventario() -> list:
    """Carga el inventario desde un archivo JSON.

    Maneja errores como archivo inexistente o JSON corrupto.

    Returns:
        list: Lista de productos. Devuelve lista vacía si hay error.

    Raises:
        None: Los errores se gestionan internamente.

    Example:
        >>> cargar_inventario()
        []
    """
    try:
        if not os.path.exists(ARCHIVO_INVENTARIO):
            return []

        with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as f:
            return json.load(f)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def guardar_inventario(items: list) -> None:
    """Guarda el inventario en un archivo JSON.

    Args:
        items (list): Lista de productos a guardar.

    Returns:
        None

    Raises:
        TypeError: Si items no es una lista.

    Example:
        >>> guardar_inventario([{"name": "Apple", "qty": 3, "price": 1.5}])
    """
    if not isinstance(items, list):
        raise TypeError("items debe ser una lista.")

    with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2) 

        
        