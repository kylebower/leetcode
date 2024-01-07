class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        cnt = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                cnt += 1
                if i>0 and nums[i+1] <= nums[i-1]:
                    nums[i+1] = nums[i]
        return cnt < 2
    