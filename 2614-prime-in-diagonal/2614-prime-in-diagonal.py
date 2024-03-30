class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        res = 0
        
        # check principal diagonal
        for i in range(n):
            cur = nums[i][i]
            if cur > res and self.isPrime(cur):
                res = cur
        
        # check secondary diagonal
        for i in range(n):
            cur = nums[i][n-1-i]
            if cur > res and self.isPrime(cur):
                res = cur
        
        # Return largest prime on a diagonal of nums. 
        # If no prime on diagonals, return 0.
        return res
    
    def isPrime(self, k: int) -> bool:
        # return True is k is prime
        # otherwise return False        
        if k < 2:
            return False
        for i in range(2, math.floor(sqrt(k)) + 1):
            if k%i == 0:
                return False
        return True
        