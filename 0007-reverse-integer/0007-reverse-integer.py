class Solution:
    def reverse(self, x: int) -> int:
        # base case:
        if abs(x) < 10:
            return x
        
        # handle negative numbers
        neg = 1
        if x < 0:
            neg = -1
            x = -x
        
        # reverse x
        y = 0
        while x > 0:
            temp = x%10
            x = x//10
            y = 10*y + temp
        
        # multiply x by neg
        x = neg*y
        
        # return x
        return x if -(2**31) < x < 2**31-1 else 0
                