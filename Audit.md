1. Falta de manejo de errores al leer JSON
📌 Código afectado
        return json.load(f)
⚠️ Riesgo
Si inventory.json está corrupto o mal formado:
el programa lanza una excepción y se detiene
Esto puede provocar:
❌ caída del sistema (DoS)
❌ pérdida de disponibilidad

✅ Propuesta de corrección
Añadir manejo de errores:

try:
    return json.load(f)
except json.JSONDecodeError:
    return []

## CONCLUSION ##: Json si control. El codigo afectado no puede leer el inventario ya que puede estar corrupto o mal formado, esto pued provocar errores. 
## Solucione Anadir un try: puede devolver un resultado correcto o vacio, dependiendo del inventario. 



🔴 2. Falta de validación de datos (CRÍTICO)
📌 Código afectado

items.append({'name': name, 'qty': qty, 'price': price})
y
item['price'] = new_price

⚠️ Riesgo
Permite:
cantidades negativas (qty < 0)
precios negativos (price < 0)
tipos incorrectos (strings, None…)

👉 Consecuencias:

❌ cálculos erróneos
❌ corrupción lógica del inventario
❌ posibles fallos en ejecución
✅ Propuesta de corrección

Validar antes de guardar:
if not isinstance(qty, int) or qty < 0:
    raise ValueError("Cantidad inválida")

if not isinstance(price, (int, float)) or price < 0:
    raise ValueError("Precio inválido")

Y lo mismo en update_price.

## CONCLUSION ##: Hay dos codigos que fallan estan sin validaciones, estos son 2 funciones con (items.). Estas funciones tienen casos edge y tienen riesgo y consecuencias de posibles fallos y errores.  
## Solucione con validaciones que no permintan numeros negativos o formatos incorrectos


🔴 3. Escritura insegura del archivo (riesgo de corrupción)
📌 Código afectado
with open(INVENTORY_FILE, 'w') as f:
    json.dump(items, f)
⚠️ Riesgo
Si el programa se interrumpe durante la escritura:
el archivo puede quedar corrupto o vacío
No hay protección frente a:
fallos del sistema
accesos concurrentes
✅ Propuesta de corrección

Usar escritura atómica:

import tempfile
import os

def save_inventory(items):
    with tempfile.NamedTemporaryFile('w', delete=False) as tmp:
        json.dump(items, tmp)
        temp_name = tmp.name
    os.replace(temp_name, INVENTORY_FILE)

👉 Esto evita archivos corruptos incluso si hay fallos

## Conclusion ##: Posible codigo afectado si hubiera algun fallo en el sistema, y datos pordrian ser corruptos, danados o perdidos. 
## Solucion que haya un documento temporal para poder evitar perdidas si hubiera fallo de sistema