# CRUD de Productos — Python

Proyecto desarrollado para la asignatura **Aplicaciones y Servicios Web** (Código: 580202009) del ITM.  
Implementa las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar un registro de productos, usando Python y almacenamiento en JSON.

---

## Estructura del proyecto

```
crud_productos/
├── productos.py        # Lógica principal del CRUD
├── test_productos.py   # Pruebas unitarias
├── productos.json      # Almacenamiento de datos (se genera automáticamente)
└── README.md           # Documentación del proyecto
```

---

## Requisitos

- Python 3.8 o superior
- No requiere librerías externas (solo módulos estándar: `json`, `os`, `unittest`)

---

## Cómo ejecutar

**1. Clonar el repositorio:**
```bash
git clone https://github.com/jpleond11/CRUD-Productos.git
cd crud_productos
```

**2. Ejecutar el proyecto:**
```bash
python productos.py
```

**3. Correr las pruebas unitarias:**
```bash
python -m unittest test_productos.py -v
```

---

## Campos del producto

Cada producto registrado contiene los siguientes campos:

| Campo       | Tipo    | Descripción                    |
|-------------|---------|--------------------------------|
| `id`        | int     | Identificador único            |
| `nombre`    | str     | Nombre del producto            |
| `descripcion` | str   | Breve descripción del producto |
| `precio`    | float   | Precio del producto            |
| `cantidad`  | int     | Cantidad disponible en stock   |

---

## Pruebas unitarias

Las pruebas cubren cada operación CRUD con al menos un caso exitoso y uno de error:

- ✅ Crear producto exitosamente
- ❌ Crear producto con ID duplicado
- ✅ Obtener lista de productos
- ❌ Buscar producto con ID inexistente
- ✅ Actualizar producto existente
- ❌ Actualizar producto inexistente
- ✅ Eliminar producto existente
- ❌ Eliminar producto inexistente

---

## Calidad del código

El análisis de calidad fue realizado con **SonarCloud**.  
Puedes ver el reporte en: `https://sonarcloud.io/project/issues?issueStatuses=OPEN%2CCONFIRMED&id=jpleond11_CRUD-Productos`

---

Autor: Juan Pablo León Duque