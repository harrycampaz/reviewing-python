import unittest

def suma(num1, num2):
    return num1 + num2 

class CajaNegraTest(unittest.TestCase):

    def test_suma_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_negativo(self):
        num_1 = -2
        num_2 = -3

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -5)

if __name__ == '__main__':
    unittest.main()
