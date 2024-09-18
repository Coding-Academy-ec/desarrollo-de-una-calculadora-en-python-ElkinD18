import unittest
import operaciones

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(operaciones.suma(3, 5), 8)
        self.assertEqual(operaciones.suma(-1, 1), 0)
        self.assertEqual(operaciones.suma(0, 0), 0)

    def test_restar(self):
        self.assertEqual(operaciones.resta(5, 3), 2)
        self.assertEqual(operaciones.resta(-1, 1), -2)
        self.assertEqual(operaciones.resta(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(operaciones.multiplicacion(3, 5), 15)
        self.assertEqual(operaciones.multiplicacion(-1, 1), -1)
        self.assertEqual(operaciones.multiplicacion(0, 0), 0)

    def test_dividir(self):
        self.assertEqual(operaciones.division(10, 2), 5)
        self.assertEqual(operaciones.division(5, 2), 2.5)
        self.assertEqual(operaciones.division(8, 4), 2)
        self.assertEqual(operaciones.division(5, 0), "Error: No se puede dividir por cero")

if __name__ == "__operaciones__":
    unittest.operaciones()
