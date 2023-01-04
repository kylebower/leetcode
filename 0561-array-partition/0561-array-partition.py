class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return sum(nums[0::2])
        