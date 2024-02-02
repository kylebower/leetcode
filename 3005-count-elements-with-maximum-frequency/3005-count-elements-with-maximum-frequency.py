class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] = d[num] + 1
            
        max_frequency = max(d.values())
        nums_with_max_feq = 0
        
        for k in d:
            if d[k] == max_frequency:
                nums_with_max_feq += 1
        
        result = max_frequency * nums_with_max_feq
        
        return result
    