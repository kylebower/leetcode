class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        while n>0 and digits[n-1] == 9:
            digits[n-1] = 0
            n -= 1
        if n == 0:
            return [1] + digits
        else:
            digits[n-1] += 1
            return digits
