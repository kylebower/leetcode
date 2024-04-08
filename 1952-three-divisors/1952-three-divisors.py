class Solution:
    def isThree(self, n: int) -> bool:
        # base case:
        if n < 4:
            return False
        
        num_divisors = 2
        for k in range(2, n//2 + 1):
            if n%k == 0:
                num_divisors += 1
                if num_divisors > 3:
                    return False
        
        return num_divisors == 3
    