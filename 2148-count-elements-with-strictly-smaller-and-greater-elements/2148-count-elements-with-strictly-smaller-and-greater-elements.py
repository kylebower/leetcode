class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_nums = min(nums)
        max_nums = max(nums)
        
        res = 0
        for num in nums:
            if num != min_nums and num != max_nums:
                res += 1
        
        return res
    