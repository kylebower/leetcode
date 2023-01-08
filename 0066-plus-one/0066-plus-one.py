class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Increment the large integer by one
        while digits[n-1] == 9:
            digits[n-1] = 0
            n -= 1
        if n == 0:
            digits = [1] + digits
        else:
            digits[n-1] += 1
            
        # return the resulting array of digits
        return digits
