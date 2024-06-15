class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for k in range(n-1):
            if nums[k] % 2 == nums[k+1] % 2:
                return False
        return True
    