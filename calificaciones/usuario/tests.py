from django.test import TestCase

from .models import Usuario


# Create your tests here.
class UsuarioClassTestCase(TestCase):
    def setUp(self):
        self.user_test = Usuario()

    def test_creacion_usuario(self):
        self.assertIsInstance(self.user_test, Usuario,
                              'Se debia generar una instancia de Usuario pero es None')

    def test_set_nombre(self):
        self.assertFalse(self.user_test.set_nombre(123),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_nombre(1.5),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_nombre(Usuario()),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_nombre(None),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_nombre(True),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_nombre(b'String'),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_nombre('Este string tiene espacios'),
                         'Debia retornar False: el string no puede tener espacios')

        self.assertFalse(self.user_test.set_nombre('1234567890_1234567890_1234567890_'),
                         'Debia retornar False: el string tiene mas de 32 caracteres')

        self.assertTrue(self.user_test.set_nombre('LoremIpsum'),
                        'Deberia retornar True: el string es valido')

        self.assertFalse(self.user_test.set_nombre('NuevoNombre'),
                         'Deberia retornar False: ya se ha definido un nombre de usuario anteriormente')

    def test_get_nombre(self):
        self.user_test.set_nombre('LoremIpsum')

        self.assertIsNone(Usuario().get_nombre(),
                          'Deberia ser None: no deberia haber ningun nombre de usuario asociado')

        self.assertIsInstance(self.user_test.get_nombre(), str,
                              'Deberia ser str: se esperaba que devuelva un str')

        self.assertEquals(self.user_test.get_nombre(), 'LoremIpsum',
                          'Deberia ser LoremIpsum: se esperaba que el nombre de usuario coincida con el guardado')

    def test_update_nombre(self):
        self.user_test.set_nombre('LoremIpsum')

        self.assertFalse(self.user_test.update_nombre(123),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.update_nombre(1.5),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.update_nombre(Usuario()),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.update_nombre(None),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.update_nombre(True),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.update_nombre(b'String'),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.update_nombre('Este string tiene espacios'),
                         'Debia retornar False: el string no puede tener espacios')

        self.assertFalse(self.user_test.update_nombre('1234567890_1234567890_1234567890_'),
                         'Debia retornar False: el string tiene mas de 32 caracteres')

        self.assertTrue(self.user_test.update_nombre('NuevoNombre'),
                        'Deberia retornar True: el string es valido')
