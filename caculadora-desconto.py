import unittest
from calculadora import CalculadoraDesconto, SemDesconto, DescontoPercentual, DescontoCupom

class TestCalculadora(unittest.TestCase):
    def test_sem_desconto(self):
        self.assertEqual(CalculadoraDesconto(SemDesconto()).calcular(100), 100)

    def test_percentual(self):
        self.assertEqual(CalculadoraDesconto(DescontoPercentual(10)).calcular(100), 90)

    def test_cupom(self):
        self.assertEqual(CalculadoraDesconto(DescontoCupom(20)).calcular(100), 80)

    def test_cupom_nao_negativo(self):
        self.assertEqual(CalculadoraDesconto(DescontoCupom(50)).calcular(30), 0)


if __name__ == "__main__":
    unittest.main()
