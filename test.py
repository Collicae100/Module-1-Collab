from mySum import sum
from fractions import Fraction
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        data = [1,2,5,3,2]
        results = sum(data)
        self.assertEqual(results, 13)

    def test_fraction(self):
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()