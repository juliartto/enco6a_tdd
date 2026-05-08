# Fase Vermelha
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


#if __name__ == "__main__":
#    unittest.main()
    
# Fase Verde
# --- Código de produção ---
class SemDesconto:
    pass

class DescontoPercentual:
    def __init__(self, percentual):
        self.percentual = percentual

class DescontoCupom:
    def __init__(self, cupom):
        self.cupom = cupom

class CalculadoraDesconto:
    def __init__(self, politica):
        self.politica = politica

    def calcular(self, valor):
        if isinstance(self.politica, SemDesconto):
            return valor
        elif isinstance(self.politica, DescontoPercentual):
            return valor - valor * self.politica.percentual / 100
        elif isinstance(self.politica, DescontoCupom):
            return max(0.0, valor - self.politica.cupom)

# --- Testes ---
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
    unittest.main(argv=[""], exit=False)
