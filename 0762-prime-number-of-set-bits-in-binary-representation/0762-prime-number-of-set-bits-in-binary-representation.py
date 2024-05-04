class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
            
        count = 0
        for k in range(left, right+1):
            if self.isPrime(self.numberSetBits(k)):
                count += 1
            
        return count
    
    def isPrime(self, k: int) -> bool:
        if k < 2:
            return False
        for j in range(2,int(sqrt(k)) + 1):
            if k%j == 0:
                return False
        return True
    
    def numberSetBits(self, k: int) -> int:
        count = 0
        while k > 0:
            count += k%2
            k //= 2
        return count
    