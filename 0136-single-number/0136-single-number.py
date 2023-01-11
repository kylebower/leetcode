class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2]) - sum(nums[1::2])
        