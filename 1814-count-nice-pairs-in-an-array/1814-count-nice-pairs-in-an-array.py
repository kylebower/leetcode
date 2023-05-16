class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            cur = n-self.rev(n)
            d[cur] = d.get(cur,0)+1
        print(d)
        nicePairs = 0
        for n in list(d.values()):
            if n >= 2:
                nicePairs += n*(n-1)/2
                nicePairs %= 1e9 + 7
        
        return int(nicePairs%(1e9 + 7))
    
    def rev(self, x: int) -> int:
        res = 0
        
        while x>0:
            res = 10*res + x%10
            x //= 10
        
        # return the reverse of the non-negative integer x
        return res
    