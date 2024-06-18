class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for k in range(len(nums) - 1):
            if nums[k] == nums[k+1]:
                res ^= nums[k]
        
        return res
    