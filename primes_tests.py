import unittest
from primes import PrimeGenerator

class PrimeGeneratorTest(unittest.TestCase):
    

    def test_primes(self):
        self.assertEqual(PrimeGenerator(10).prime_generator(), [2, 3, 5, 7])
        self.assertEqual(PrimeGenerator(20).prime_generator(), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_zero(self):
        self.assertEqual(PrimeGenerator(0).prime_generator(), "0 is not a prime number")

    def test_one(self):
        self.assertEqual(PrimeGenerator(1).prime_generator(), "1 is not a prime number")

    def test_non_integer(self):
        self.assertEqual(PrimeGenerator('a').prime_generator(), "Enter an integer")

    def test_non_negative(self):
        self.assertEqual(PrimeGenerator(-5).prime_generator(), "Number should be a positive integer")


if __name__ == '__main__':
    unittest.main()
