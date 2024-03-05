class Solution:
    def toHex(self, num: int) -> str:
            
        # base case:
        if num == 0:
            return '0'
        
        if num < 0:
            num += 2**32
        
        res = ''
        while num > 0:
            last_digit = num%16
            res = self.hexidecimal(last_digit) + res
            num //= 16
        
        return res
    
    def hexidecimal(self, digit: int) -> str:
        # define dict
        d = defaultdict(int)
        for k in range(10,17):
            d[k] = chr(ord('a') + k - 10)
        if digit < 10:
            return str(digit)
        else:
            return d[digit]
        