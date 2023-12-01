class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        noninc = True
        nondec = True
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nondec = False
            elif nums[i] < nums[i+1]:
                noninc = False
        return noninc or nondec
    