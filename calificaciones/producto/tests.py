from django.test import TestCase
from .models import Producto


# Create your tests here.
class ProductoClassTestCase(TestCase):
    def setUp(self):
        self.producto_test = Producto()

    def test_producto_nombre(self):
        producto = self.producto_test

        self.assertEqual(producto.nombre, '',
                         'El producto no deberia tener ningun nombre al principio')

        producto.nombre = 'Televisor'

        self.assertEqual(producto.nombre, 'Televisor',
                         'El producto deberia tener como nombre "Televisor"')

    def test_producto_fabricante(self):
        producto = self.producto_test

        self.assertEqual(producto.fabricante, '',
                         'El producto no deberia tener ningun fabricante al principio')

        producto.fabricante = 'Generico 123'

        self.assertEqual(producto.fabricante, 'Generico 123',
                         'El producto deberia tener como fabricante "Generico 123"')

    def test_producto_precio(self):
        producto = self.producto_test

        self.assertEqual(producto.precio, None,
                         'El producto no deberia tener ningun precio al principio')

        producto.precio = 150.75

        self.assertEqual(producto.precio, 150.75,
                         'El producto deberia tener como precio 150.75')

    def test_producto_categoria(self):
        producto = self.producto_test

        self.assertEqual(producto.categoria, 'Otros',
                         'El producto deberia tener como categoria Otros')

        producto.categoria = 'EL'

        self.assertEqual(producto.categoria, 'Electronica',
                         'El producto deberia tener como categoria Electronica')

    def test_prodcuto(self):
        producto = self.producto_test

        producto.nombre = 'Proyector 2200'
        producto.precio = 1250.66
        producto.categoria = 'EL'
        producto.fabricante = 'Digital Display'

        self.assertEqual(producto.nombre, 'Proyector 2200')
        self.assertEqual(producto.precio, 1250.66)
        self.assertEqual(producto.categoria, 'Electronica')
        self.assertEqual(producto.fabricante, 'Digital Display')
