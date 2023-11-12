class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i in range(n):
            res[i] = len(set(nums[:i+1])) - len(set(nums[i+1:]))
        return res
    