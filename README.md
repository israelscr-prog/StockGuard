# 📦 StockGuard

![CI](https://github.com/israelscr-prog/StockGuard/actions/workflows/ci.yml/badge.svg)

## 🧾 Descripción

**StockGuard** es un sistema de gestión de inventario desarrollado en Python 3.12+, diseñado para garantizar la integridad de los datos mediante validaciones estrictas, testing automatizado y un pipeline de integración continua.

Permite registrar productos con:

- Nombre  
- Cantidad  
- Precio  

Asegurando que:

- ❌ No existan cantidades negativas  
- ❌ No existan precios inválidos  
- ✅ Los datos sean consistentes y persistentes en JSON  

---

## 🎯 Objetivo del proyecto

Este proyecto parte de un código heredado con vulnerabilidades y ausencia de buenas prácticas.  
El objetivo ha sido transformarlo aplicando:

- 🔍 Auditoría de seguridad  
- 🧪 Testing automatizado con mocks  
- 📚 Documentación técnica  
- ⚙️ Pipeline CI/CD  

👉 Demostrando cómo la IA puede apoyar el ciclo completo de calidad del software.

---

## 🧩 Módulos principales

| Módulo | Descripción |
|--------|------------|
| `models.py` | Define la clase `Item` con validaciones |
| `storage.py` | Carga y guarda inventario en JSON |
| `validator.py` | Funciones de validación reutilizables |
| `stockguard.py` | Lógica principal heredada |
| `safe_stockguard.py` | Wrapper seguro del sistema |

---

## ⚙️ Instalación

**Requisitos:** Python 3.12+

```bash
# 1. Clonar repositorio
git clone https://github.com/israelscr-prog/StockGuard.git
cd StockGuard

# 2. Crear entorno virtual
python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar paquete
pip install -e .
🧪 Testing

Ejecutar todos los tests:

python -m pytest -v

Con cobertura:

python -m pytest --cov=stockguard -v
📁 Suite de tests
Archivo	Descripción
test_models.py	Validación de creación de Item
test_storage.py	Mock de archivos y JSON
test_validator.py	Casos base y edge cases
🔍 Linting
python -m flake8 . --exclude=.venv,venv,__pycache__,.git,stockguard.egg-info --max-line-length=88
🔁 CI/CD

El proyecto incluye un pipeline en GitHub Actions:

📍 .github/workflows/ci.yml

Se ejecuta en cada:

push
pull_request a main
🔧 Pasos del pipeline:
Checkout del repositorio
Setup Python 3.12
Instalación de dependencias
Análisis con Flake8
Ejecución de tests con pytest

📸 Ejemplo: imagenes\image.png
g

🔒 Seguridad y mejoras aplicadas

Se han corregido vulnerabilidades críticas del código heredado:

Validación de datos (cantidad y precio)
Manejo de errores en JSON corrupto
Control de archivo inexistente
Mejora en robustez del sistema

📄 Ver detalles en: AUDIT.md

#🤖 Uso de IA

Este proyecto ha sido desarrollado con apoyo de IA #(Perplexity AI, ChatGPT y Sonnet4.6) en:

Diagnóstico de errores
Generación de tests
Configuración del pipeline CI/CD
Documentación técnica
👨‍💻 Rol del desarrollador
Validación de soluciones propuestas
Ajuste al contexto real del proyecto
Resolución de conflictos (case-sensitive, imports, etc.)
Pruebas manuales y verificación final

👉 La IA actúa como asistente, no como sustituto.

#🧠 Reflexión

La combinación de IA + criterio humano permite:

Detectar errores más rápido
Aplicar buenas prácticas
Mejorar la calidad del software

Pero siempre requiere supervisión y decisiones técnicas del desarrollador.

📂 Estructura del proyecto
StockGuard/
├── .github/workflows/ci.yml
├── stockguard/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   ├── validator.py
│   ├── stockguard.py
│   └── safe_stockguard.py
├── tests/
│   ├── test_models.py
│   ├── test_storage.py
│   └── test_validator.py
├── pyproject.toml
├── setup.cfg
├── requirements.txt
├── AUDIT.md
└── README.md
📄 Licencia

Este proyecto está bajo licencia MIT.


---

## 🔥 Mejoras clave que te hice

- Lenguaje más profesional  
- Estructura clara (empresa / técnico)  
- Tablas limpias  
- Separación visual  
- Eliminé repeticiones  
- Mejor narrativa del proyecto  
- Más “nivel GitHub real”  

---
