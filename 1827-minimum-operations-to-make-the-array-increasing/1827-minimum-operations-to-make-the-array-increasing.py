class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        prev = nums[0]
        for k in range(1,len(nums)):
            if nums[k] <= prev:
                res += prev - nums[k] + 1
            prev = max(nums[k], prev + 1)
        return res
    