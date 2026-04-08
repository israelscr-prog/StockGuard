import pytest
from stockguard.models import Item

def test_creacion_valida():
    """Prueba: creación válida de un Item."""
    item = Item(nombre="Manzana", cantidad=5, precio=1.5)

    assert item.nombre == "Manzana"
    assert item.cantidad == 5
    assert item.precio == 1.5


def test_cantidad_cero():
    """Prueba: cantidad = 0 debe lanzar ValueError."""
    with pytest.raises(ValueError):
        Item(nombre="Manzana", cantidad=0, precio=1.5)


def test_cantidad_negativa():
    """Prueba: cantidad negativa debe lanzar ValueError."""
    with pytest.raises(ValueError):
        Item(nombre="Manzana", cantidad=-5, precio=1.5)


def test_precio_cero():
    """Prueba: precio = 0 debe lanzar ValueError."""
    with pytest.raises(ValueError):
        Item(nombre="Manzana", cantidad=5, precio=0)


def test_precio_negativo():
    """Prueba: precio negativo debe lanzar ValueError."""
    with pytest.raises(ValueError):
        Item(nombre="Manzana", cantidad=5, precio=-1)


def test_precio_minimo_valido():
    """Caso extremo: precio muy pequeño pero válido."""
    item = Item(nombre="Manzana", cantidad=1, precio=0.001)
    assert item.precio == 0.001


def test_cantidad_grande():
    """Caso extremo: cantidad muy grande."""
    item = Item(nombre="Manzana", cantidad=1_000_000, precio=1.0)
    assert item.cantidad == 1_000_000