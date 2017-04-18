class PrimeGenerator():

    def __init__(self, n):
        self.n = n

    def isprime(self,n):
        for x in range(2,n):
            if n%x == 0:
                return False
        return True

    def prime_generator(self):
        if not (isinstance(self.n, int)): return "Enter an integer"
        if self.n < 0: return 'Number should be a positive integer'
        if self.n == 0: return "0 is not a prime number"
        if self.n == 1: return "1 is not a prime number"

        return [x for x in range(2,self.n+1) if self.isprime(x)]
