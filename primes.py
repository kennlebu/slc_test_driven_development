class PrimeGenerator(object):
    def isprime(n):
        for x in range(2,n):
            if n%x == 0:
                return False
        return True

    def prime_generator(n):
        if not (isinstance(n, int)): return "Enter an integer"
        if not (isinstance(n, int)): return "Enter an integer"
        if n == 0: return "0 is not a prime number"
        if n == 1: return "1 is not a prime number"

        return [x for x in range(2,n+1) if isprime(x)]


##import unittest
##class prime_tester(unittest.TestCase):
##    def test_if_primes(self):
##        self.assertEqual(prime_generator(10), [2, 3, 5, 7])
##        self.assertEqual(prime_generator(20), [2, 3, 5, 7, 11, 13, 17, 19])
##
##
##
##def main():
##    prime_tester.test_if_primes()

print(PrimeGenerator.prime_generator(0))
