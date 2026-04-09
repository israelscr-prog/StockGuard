# 🔍 Auditoría de Seguridad – StockGuard

## 1. Falta de manejo de errores al leer JSON

### 📌 Código afectado
```python
return json.load(f)
⚠️ Riesgo

Si el archivo inventory.json está corrupto o mal formado:

El programa lanza una excepción (JSONDecodeError)
La ejecución se interrumpe inesperadamente

Esto puede provocar:
❌ Caída del sistema (Denegación de servicio - DoS)
❌ Pérdida de disponibilidad
✅ Propuesta de corrección

Implementar manejo de excepciones:

try:
    return json.load(f)
except json.JSONDecodeError:
    return []
    
###🧾 Conclusión

La falta de control sobre la lectura del JSON hace que el sistema sea frágil ante datos corruptos.
La solución implementada garantiza que, en caso de error, el sistema continúe funcionando devolviendo un estado seguro (lista vacía).
```

## 2. Falta de validación de datos (CRÍTICO) 


### 📌 Código afectado

```python

items.append({'name': name, 'qty': qty, 'price': price})
item['price'] = new_price

⚠️ Riesgo

El sistema permite la entrada de datos inválidos:

Cantidades negativas (qty < 0)
Precios negativos (price < 0)
Tipos incorrectos (str, None, etc.)
👉 Consecuencias
❌ Cálculos incorrectos
❌ Corrupción lógica del inventario
❌ Posibles errores en ejecución
✅ Propuesta de corrección

Validar los datos antes de almacenarlos:

if not isinstance(qty, int) or qty <= 0:
    raise ValueError("Cantidad inválida")

if not isinstance(price, (int, float)) or price <= 0:
    raise ValueError("Precio inválido")

Aplicar las mismas validaciones en funciones de actualización (update_price, etc.).


###🧾 Conclusión

La ausencia de validaciones representa un riesgo crítico para la integridad del sistema.
La solución implementada garantiza que solo se acepten datos válidos, evitando inconsistencias y errores en el inventario.

```


## 3. Escritura insegura del archivo (riesgo de corrupción)
### 📌 Código afectado
```python

with open(INVENTORY_FILE, 'w') as f:
    json.dump(items, f)
⚠️ Riesgo

Si el programa se interrumpe durante la escritura:

El archivo puede quedar vacío o corrupto
No existe protección frente a:
Fallos del sistema
Interrupciones inesperadas
Escrituras concurrentes

✅ Propuesta de corrección

Implementar escritura atómica:

import tempfile
import os

def save_inventory(items):
    with tempfile.NamedTemporaryFile('w', delete=False) as tmp:
        json.dump(items, tmp)
        temp_name = tmp.name
    os.replace(temp_name, INVENTORY_FILE)

👉 Ventajas
Evita archivos corruptos
Garantiza consistencia de datos
Mejora la robustez del sistema


###🧾 Conclusión

La escritura directa en el archivo supone un riesgo de corrupción de datos.
El uso de escritura atómica asegura que el archivo solo se actualice cuando la operación se completa correctamente.

```
# 4. ✅ Conclusión general 

```python

#Se han identificado y corregido tres vulnerabilidades clave:
Falta de manejo de errores
Falta de validación de datos (crítica)
Escritura insegura

Las mejoras implementadas aumentan significativamente:

🔒 Seguridad
📊 Integridad de datos
⚙️ Robustez del sistema

👉 El sistema pasa de ser vulnerable a ser fiable y preparado para producción.