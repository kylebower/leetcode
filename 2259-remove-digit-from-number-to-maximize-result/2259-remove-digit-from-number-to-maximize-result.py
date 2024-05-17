class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        cur_max = 0
        
        for i, num in enumerate(number):
            if num == digit:
                cur_max = max(cur_max, int(number[:i] + number[i+1:]))
        
        return str(cur_max)
            