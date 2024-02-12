class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            
        sorted_keys = sorted(list(d.keys()))
        
        res = 0
        
        for i, key in enumerate(sorted_keys):
            res += i*d[key]
            
        return res
        