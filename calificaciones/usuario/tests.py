from django.test import TestCase
from django.utils import timezone

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

    def test_set_contrasenna(self):
        self.assertFalse(self.user_test.set_contrasenna(123),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_contrasenna(1.5),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_contrasenna(Usuario()),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_contrasenna(None),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_contrasenna(True),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_contrasenna(b'String'),
                         'Debia retornar False: solo se acepta str')

        self.assertFalse(self.user_test.set_contrasenna('Este string tiene espacios'),
                         'Debia retornar False: el string no puede tener espacios')

        self.assertFalse(self.user_test.set_contrasenna('0101010'),
                         'Debia retornar False: el string tiene menos de 8 caracteres')

        self.assertTrue(self.user_test.set_contrasenna('12345678'),
                        'Deberia retornar True: el string es valido')

    def test_iniciar_sesion(self):
        self.user_test.set_contrasenna('1234567A')

        self.assertFalse(self.user_test.iniciar_sesion('1234567a'),
                         'Deberia retornar False: la contraseñas son case sentive')

        self.assertIsNone(self.user_test.get_ultimo_login(),
                          'Deberia ser None: el usuario nunca inicio sesion')

        self.assertTrue(self.user_test.iniciar_sesion('1234567A'),
                        'Deberia retornar True: ambas contraseñas son iguales')

        self.assertEquals(self.user_test.get_ultimo_login(), timezone.now().date(),
                          'Deberia coincidir: el usuario inicio sesion correctamente y la fecha debe ser actual')

    def test_get_fecha_creacion(self):
        self.assertEquals(self.user_test.get_fecha_creacion(), timezone.now().date(),
                          'La fecha de creacion debe coincidir con la fecha actual')