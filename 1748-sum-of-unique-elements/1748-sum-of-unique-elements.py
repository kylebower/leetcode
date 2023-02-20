class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # define dictionary of occurances
        d = {}
        for n in nums:
            d[n] = d.get(n,0)+1
        
        # sum unique elements
        res = 0
        for key in list(d.keys()):
            if d[key] == 1:
                res += key
        
        # return sum
        return res
