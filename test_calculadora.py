import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):    
        self.assertEqual(soma(5, 5), 10)
        
    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (1, 1 ,2),
            (5, 1 ,6),
            (10, 2 ,12),
            (100, 1 ,101),
            (3, 3 ,6),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

unittest.main(verbosity=2)