import unittest
from primes import PrimeGenerator

class PrimeGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.primes = PrimeGenerator()

    def test_primes(self):
        self.assertEqual(self.primes.prime_generator(10), [2, 3, 5, 7], msg="Not all numbers are prime")
        self.assertEqual(self.primes.prime_generator(20), [2, 3, 5, 7, 11, 13, 17, 19], msg="Not all numbers are prime")

    
