class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num_digits = 0
        res = 0
        
        while n > 0:
            res += n%10 * (1 if num_digits%2==0 else -1)
            n //= 10
            num_digits += 1
        
        return res * (-1 if num_digits%2==0 else 1)
    