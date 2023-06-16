class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return len(set([nums[i]+nums[n-i-1] for i in range(n//2)]))
        