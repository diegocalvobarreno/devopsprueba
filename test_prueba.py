from unittest import TestCase
import prueba

class Test(TestCase):
    def test_sumar(self):
        self.assertEqual(prueba.sumar(5, 5), 10)
        self.assertEqual(prueba.sumar(4, 6), 10)
