import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        self.assertEqual(area(5), 25)

    def test_area_negative(self):
        self.assertEqual(area(-3), 'error')

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(4), 16)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-2), 'error')

if __name__ == "__main__":
    unittest.main()
