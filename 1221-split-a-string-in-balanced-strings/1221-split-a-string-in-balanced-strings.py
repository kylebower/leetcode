class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_l = 0
        num_r = 0
        res = 0
        
        for c in s:
            if c == 'L':
                num_l += 1
            else:
                num_r += 1
            if num_l == num_r:
                res += 1
        
        return res
        