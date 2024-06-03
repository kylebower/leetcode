class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sort = sorted(nums[1:])
        return sum(sort[:2]) + nums[0]
    