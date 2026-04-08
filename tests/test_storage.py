import pytest
import json
from stockguard.Storage import cargar_inventario, guardar_inventario

# -----------------------------------
# Tests para cargar_inventario()
# -----------------------------------

def test_archivo_inexistente(mocker):
    """Si el archivo no existe, cargar_inventario() devuelve lista vacía."""
    mocker.patch("os.path.exists", return_value=False)
    resultado = cargar_inventario()
    assert resultado == []

def test_archivo_corrupto(mocker):
    """Si el JSON es inválido, cargar_inventario() devuelve lista vacía."""
    mocker.patch("os.path.exists", return_value=True)
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    mocker.patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0))
    
    resultado = cargar_inventario()
    assert resultado == []

def test_archivo_valido(mocker):
    """Carga un JSON válido correctamente."""
    datos = [{"nombre": "Apple", "cantidad": 10, "precio": 1.5}]
    mocker.patch("os.path.exists", return_value=True)
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    mocker.patch("json.load", return_value=datos)
    
    resultado = cargar_inventario()
    assert resultado == datos

# -----------------------------------
# Tests para guardar_inventario()
# -----------------------------------

def test_guardado_con_indent(mocker):
    """Verifica que guardar_inventario llame a json.dump con indent=2."""
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    mock_json_dump = mocker.patch("json.dump")
    
    items = [{"nombre": "Banana", "cantidad": 5, "precio": 0.99}]
    guardar_inventario(items)
    
    # Verificar que json.dump se llamó con indent=2
    args, kwargs = mock_json_dump.call_args
    assert kwargs.get("indent") == 2
    assert args[0] == items