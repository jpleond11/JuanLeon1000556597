import unittest
import os
from productos import (
    crear_producto,
    obtener_productos,
    obtener_producto_por_id,
    actualizar_producto,
    eliminar_producto,
)

ARCHIVO = "productos.json"


class TestCRUDProductos(unittest.TestCase):

    def setUp(self):
        if os.path.exists(ARCHIVO):
            os.remove(ARCHIVO)

    # --- CREAR PRODUCTO --- #
    def test_crear_producto_exitoso(self):
        p = crear_producto(1, "PC Portátil", "Laptop gamer", 3500000, 10)
        self.assertEqual(p["nombre"], "PC Portátil")

    def test_crear_producto_id_duplicado(self):
        crear_producto(1, "PC Portátil", "Laptop gamer", 3500000, 10)
        with self.assertRaises(ValueError):
            crear_producto(1, "Otro", "Desc", 1000, 5)

    # --- LEER PRODUCTO ---
    def test_obtener_productos_exitoso(self):
        crear_producto(1, "Mouse", "Mouse inalámbrico", 80000, 20)
        productos = obtener_productos()
        self.assertEqual(len(productos), 1)

    def test_obtener_producto_por_id_no_existe(self):
        with self.assertRaises(ValueError):
            obtener_producto_por_id(99)

    # --- ACTUALIZAR PRODUCTO ---
    def test_actualizar_producto_exitoso(self):
        crear_producto(1, "Teclado", "Mecánico", 250000, 15)
        actualizado = actualizar_producto(1, {"precio": 270000})
        self.assertEqual(actualizado["precio"], 270000)

    def test_actualizar_producto_no_existe(self):
        with self.assertRaises(ValueError):
            actualizar_producto(99, {"precio": 100})

    # --- ELIMINAR PRODUCTO ---
    def test_eliminar_producto_exitoso(self):
        crear_producto(1, "Monitor", "4K", 1200000, 5)
        resultado = eliminar_producto(1)
        self.assertTrue(resultado)

    def test_eliminar_producto_no_existe(self):
        with self.assertRaises(ValueError):
            eliminar_producto(99)

    # --- OBTENER UN PRODUCTO POR ID EXITOSO ---
    def test_obtener_producto_por_id_exitoso(self):
        crear_producto(5, "Audífonos", "Bluetooth inalámbrico", 320000, 8)
        p = obtener_producto_por_id(5)
        self.assertEqual(p["nombre"], "Audífonos")


if __name__ == "__main__":
    unittest.main()
