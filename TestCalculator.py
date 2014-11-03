import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def testsuma(self):
        cal = Calculator()
        self.assertEqual(4, cal.suma(2, 2))

    def testsuma(self):
        cal = Calculator()
        self.assertEqual(23, cal.suma(13, 10))

    def testsuma(self):
        cal = Calculator()
        self.assertEqual(54, cal.suma(28, 26))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(45, cal.resta(78, 33))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(13, cal.resta(35, 12))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(2, cal.resta(46, 44))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(32, cal.multiplicacion(8, 4))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(24, cal.multiplicacion(6, 4))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(84, cal.multiplicacion(14, 6))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(2, cal.division(45, 21))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(3, cal.division(1254, 456))

    def testresta(self):
        cal = Calculator()
        self.assertEqual(279, cal.division(898542, 3216))
if __name__ == '__main__':
    unittest.main()
