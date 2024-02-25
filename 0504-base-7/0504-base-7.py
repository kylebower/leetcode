class Solution:
    def convertToBase7(self, num: int) -> str:
        # base case
        if num == 0:
            return "0"
        
        negative = (num < 0)
        num = abs(num)
        base7 = ''
        while num > 0:
            digit = num % 7
            base7 = str(digit) + base7
            num //= 7
        if negative:
            return '-' + base7
        else:
            return base7
        