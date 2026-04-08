import pytest
from stockguard.validator import validar_cantidad, validar_precio

# -----------------------------------
# Tests para validar_cantidad()
# -----------------------------------

def test_cantidad_valida():
    """Caso base: cantidad positiva válida."""
    assert validar_cantidad(10) is True

def test_cantidad_cero():
    """Caso límite: cantidad = 0 debe lanzar ValueError."""
    with pytest.raises(ValueError):
        validar_cantidad(0)

def test_cantidad_negativa():
    """Caso límite: cantidad negativa debe lanzar ValueError."""
    with pytest.raises(ValueError):
        validar_cantidad(-5)

def test_cantidad_muy_grande():
    """Edge case: cantidad extremadamente alta."""
    assert validar_cantidad(1_000_000) is True

def test_cantidad_minima_positiva():
    """Edge case: cantidad mínima positiva."""
    assert validar_cantidad(1) is True

# -----------------------------------
# Tests para validar_precio()
# -----------------------------------

def test_precio_valido():
    """Caso base: precio positivo válido."""
    assert validar_precio(9.99) is True

def test_precio_cero():
    """Caso límite: precio = 0 debe lanzar ValueError."""
    with pytest.raises(ValueError):
        validar_precio(0)

def test_precio_negativo():
    """Caso límite: precio negativo debe lanzar ValueError."""
    with pytest.raises(ValueError):
        validar_precio(-1.5)

def test_precio_muy_pequeno():
    """Edge case: precio extremadamente pequeño positivo."""
    assert validar_precio(0.0001) is True

def test_precio_muy_grande():
    """Edge case: precio extremadamente grande."""
    assert validar_precio(1_000_000.0) is True
