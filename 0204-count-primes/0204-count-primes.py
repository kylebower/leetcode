class Solution:
    def countPrimes(self, n: int) -> int:
        # Base case
        if n < 2:
            return 0
        
        primes = [1]*n  # 1 indicates prime, 0 indicates not prime
        primes[0] = 0   # 0 is not prime
        primes[1] = 0   # 1 is not prime
        
        # iterate to find numbers that are not prime
        for p in range(2,int(n**0.5)+1):
            primes[2*p:n:p] = [0]*len(primes[2*p:n:p])            
        
        # return number of prime numbers that are strictly less than n
        return sum(primes)
    