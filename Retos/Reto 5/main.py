import unittest, geometria, view

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass() -> OK \n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass() -> OK \n")

    def setUp(self):
        print("\n\nsetUp() -> OK")

    def test_areaCuadrado(self):
        result = geometria.Geometria.areaCuadrado(self, 5)
        self.assertEqual(result, 25)
        print("test_areaCuadrado() -> OK")

    def test_areaCirculo(self):
        result = geometria.Geometria.areaCirculo(self, 4)
        self.assertEqual(result, 50.2656)
        print("test_areaCirculo() -> OK")

    def test_areaTriangulo(self):
        result = geometria.Geometria.areaTiangulo(self, 5, 6)
        self.assertEqual(result, 15)
        print("test_areaTriangulo() -> OK")

    def test_areaRectangulo(self):
        result = geometria.Geometria.areaRectangulo(self, 5, 9)
        self.assertEqual(result, 45)
        print("test_areaRectangulo() -> OK")

    def test_areaPentagano(self):
        result = geometria.Geometria.areaPentagono(self, 6, 6)
        self.assertEqual(result, 18)
        print("test_areaPentagono() -> OK")

    def test_areaRombo(self):
        result = geometria.Geometria.areaRombo(self, 3, 4)
        self.assertEqual(result, 6)
        print("test_areaRombo() -> OK")

    def test_areaRomboide(self):
        result = geometria.Geometria.areaRomboide(self, 5, 6)
        self.assertEqual(result, 30)
        print("test_areaRomboide() -> OK")

    def test_areaTrapecio(self):
        result = geometria.Geometria.areaTrapecio(self, 4, 5, 4)
        self.assertEqual(result, 18)
        print("test_areaTrapecio() -> OK")

    def tearDown(self):
        print("tearDown() -> OK \n")

if __name__ == '__main__':
    g = geometria.Geometria(2.00, 3.10, 4.00)
    v = view.View()
    v.select(g)