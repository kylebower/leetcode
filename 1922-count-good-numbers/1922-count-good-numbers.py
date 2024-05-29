class Solution:
    def countGoodNumbers(self, n: int) -> int:
        numPrimeDigits = 4
        numEvenDigits = 5
        
        rem = n % 2
        
        res = pow(numPrimeDigits*numEvenDigits, n//2, 10**9 + 7)
        
        if rem == 1:
            res *= 5
            res %= (10**9 + 7)
        
        return res
    