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
