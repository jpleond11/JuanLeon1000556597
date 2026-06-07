import json
import os

# Módulo principal para la gestión de productos mediante operaciones CRUD #
ARCHIVO = "productos.json"


def cargar_productos():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_productos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)


# Crear Producto#
def crear_producto(id, nombre, descripcion, precio, cantidad):
    productos = cargar_productos()
    if any(p["id"] == id for p in productos):
        raise ValueError(f"Ya existe un producto con id {id}")
    producto = {
        "id": id,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "cantidad": cantidad,
    }
    productos.append(producto)
    guardar_productos(productos)
    return producto


# Leer Producto#
def obtener_productos():
    return cargar_productos()


def obtener_producto_por_id(id):
    productos = cargar_productos()
    for p in productos:
        if p["id"] == id:
            return p
    raise ValueError(f"Producto con id {id} no encontrado")


# Actualizar Producto#
def actualizar_producto(id, datos):
    productos = cargar_productos()
    for p in productos:
        if p["id"] == id:
            p.update(datos)
            guardar_productos(productos)
            return p
    raise ValueError(f"Producto con id {id} no encontrado")


# Eliminar Producto#
def eliminar_producto(id):
    productos = cargar_productos()
    nuevos = [p for p in productos if p["id"] != id]
    if len(nuevos) == len(productos):
        raise ValueError(f"Producto con id {id} no encontrado")
    guardar_productos(nuevos)
    return True


# Obtener un producto por ID exitoso#
def test_obtener_producto_por_id_exitoso(self):
    crear_producto(5, "Audífonos", "Bluetooth inalámbrico", 320000, 8)
    p = obtener_producto_por_id(5)
    self.assertEqual(p["nombre"], "Audífonos")
