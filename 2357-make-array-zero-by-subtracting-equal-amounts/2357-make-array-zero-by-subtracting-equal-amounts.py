class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
        
        return len(d.keys()) - (min(d) == 0)