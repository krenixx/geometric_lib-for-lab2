import unittest
from circle import area, perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_negative(self):
        self.assertAlmostEqual(area(-10), 'error')

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(2), 2 * math.pi * 2)

    def test_perimeter_negative(self):
        self.assertAlmostEqual(perimeter(-5), 'error')

if __name__ == "__main__":
    unittest.main()
