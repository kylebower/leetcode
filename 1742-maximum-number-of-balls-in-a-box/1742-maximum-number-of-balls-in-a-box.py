class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        # define dict d[box number] = number of balls in box
        d = {}
        for k in range(lowLimit, highLimit+1):
            digit_sum = self.sumDigits(k)
            d[digit_sum] = d.get(digit_sum, 0) + 1
        
        # number of balls in the box with the most balls
        return max(list(d.values()))
    
    def sumDigits(self, k):
        res = 0
        while k > 0:
            res += k%10
            k //= 10
        return res
    