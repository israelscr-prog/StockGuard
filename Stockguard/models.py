from dataclasses import dataclass

@dataclass
class Item:
    """Clase que representa un item en inventario.

    Args:
        nombre (str): Nombre del item.
        cantidad (int): Cantidad disponible, debe ser mayor que 0.
        precio (float): Precio unitario, debe ser mayor que 0.

    Raises:
        ValueError: Si cantidad <= 0 o precio <= 0.
    """
    nombre: str
    cantidad: int
    precio: float

    def __post_init__(self):
        if self.cantidad <= 0:
            raise ValueError("cantidad debe ser mayor que 0")
        if self.precio <= 0:
            raise ValueError("precio debe ser mayor que 0")