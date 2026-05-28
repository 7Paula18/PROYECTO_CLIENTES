# Proyecto Clientes — API REST

**Aprendiz:** María Paula Aguilera Reina  
**Ficha:** 3407184

---

## Descripción

API REST desarrollada con **FastAPI** para la gestión de clientes, facturas y transacciones. Permite realizar operaciones CRUD sobre clientes y registrar facturas y transacciones mediante endpoints HTTP.

---

## Estructura de Carpetas

```
📦 proyecto-clientes/
├── 📁 modelos/                  # Modelos de datos con Pydantic
│   ├── __init__.py
│   ├── clientes.py              # Modelos Cliente y ClienteCrear
│   ├── facturas.py              # Modelo Factura
│   └── transacciones.py        # Modelo Transaccion
├── 📁 routers/                  # Rutas y lógica de cada recurso
│   ├── __init__.py
│   ├── clientes.py              # CRUD completo de clientes
│   ├── facturas.py              # Listar y crear facturas
│   └── transacciones.py        # Listar y crear transacciones
├── 📄 main.py                   # Punto de entrada de la aplicación
├── 📄 database.py               # Configuración futura de base de datos
├── 📄 requirements.txt          # Dependencias del proyecto
├── 📄 pyproject.toml            # Configuración del proyecto
└── 📄 README.md
```

---

## Endpoints disponibles

### Clientes
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/clientes` | Listar todos los clientes |
| POST | `/clientes` | Crear un nuevo cliente |
| GET | `/clientes/{id}` | Obtener un cliente por ID |
| PUT | `/clientes/{id}` | Editar un cliente existente |
| DELETE | `/clientes/{id}` | Eliminar un cliente |

### Facturas
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/facturas` | Listar todas las facturas |
| POST | `/facturas` | Crear una nueva factura |

### Transacciones
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/transacciones` | Listar todas las transacciones |
| POST | `/transacciones` | Crear una nueva transacción |

---

## Historial de Actividades

| Fecha | Descripción |
|-------|-------------|
| 2025-05-20 | Creación del proyecto con FastAPI y estructura de carpetas |
| 2025-05-21 | Definición de modelos Pydantic: `Cliente`, `Factura`, `Transaccion` |
| 2025-05-22 | Implementación del CRUD completo para clientes (GET, POST, PUT, DELETE) |
| 2025-05-23 | Implementación de routers para facturas y transacciones |
| 2025-05-24 | Separación del modelo `ClienteCrear` para manejo correcto del ID |
| 2025-05-25 | Registro de `routers` en `main.py` y prueba de endpoints |
| 2025-05-26 | Documentación del proyecto |

> *(Ajusta las fechas según tu historial real de commits)*

---

## Requisitos Previos

- Python 3.14 o superior
- pip

---

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/proyecto-clientes.git
cd proyecto-clientes
```

### 2. Crear el entorno virtual

```bash
# En Windows
python -m venv venv

# En macOS / Linux
python3 -m venv venv
```

### 3. Activar el entorno virtual

```bash
# En Windows
venv\Scripts\activate

# En macOS / Linux
source venv/bin/activate
```

Sabrás que está activo porque verás `(venv)` al inicio de tu terminal.

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`  
Documentación interactiva en: `http://127.0.0.1:8000/docs`

---

## Desactivar el entorno virtual

```bash
deactivate
```

---

*Aprendiz SENA — Ficha 3407184*
