class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n):
            digits[n-1-i] += 1
            if digits[n-1-i] < 10:
                return digits
            else:
                digits[n-1-i] = 0
                if i == n-1:
                    return [1] + digits
            
        # return incremented array
        return digits