import unittest
from square import *


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        res = area(5.239)
        self.assertAlmostEqual(res, 27.447121, delta=0.1)

    def test_zero_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_float_perimetr(self):
        res = perimeter(5.239)
        self.assertAlmostEqual(res, 20.956, delta=0.1)
