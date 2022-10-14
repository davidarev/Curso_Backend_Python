import unittest
import kata4_funciones as funciones

class Test_Calculadora(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass() -> OK")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass() -> OK")

    def setUp(self):
        print("setUp() -> OK")

    def test_sumar(self):
        result = funciones.sumar(15, 5)
        self.assertEqual(result, 20)
        print("test_suma() -> OK \n")

    def test_resta(self):
        result = funciones.restar(15, 5)
        self.assertEqual(result, 10)
        print("test_resta() -> OK \n")

    def test_doblar(self):
        result = funciones.doblar(7)
        self.assertEqual(result, 14)
        print("test_doblar() -> OK \n")

    def test_dividir(self):
        result = funciones.dividir(15, 5)
        self.assertEqual(result, 3)
        print("test_dividir() -> OK \n")

    def test_multiplicar(self):
        result = funciones.multiplicar(15, 5)
        self.assertEqual(result, 75)
        print("test_multiplicar() -> OK \n")

    def test_esPar(self):
        result = funciones.es_par(30)
        self.assertEqual(result, 1)
        print("test_esPar() -> OK \n")

    def test_cuadrado(self):
        result = funciones.cuadrado(7)
        self.assertEqual(result, 49)
        print("test_cuadrado() -> OK \n")

    def test_raiz(self):
        result = funciones.raiz(49)
        self.assertEqual(result, 7)
        print("test_raiz() -> OK \n")

    def tearDown(self):
        print("tearDown() -> OK")

if __name__ == "__main__":
    unittest.main()