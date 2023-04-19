class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        nums.sort()
        
        n = len(nums)
        L = 0
        R = n-1
        while L < R:
            if -nums[L] == nums[R]:
                return nums[R]
            elif nums[L]>0 or nums[R]<0:
                return -1
            elif -nums[L] < nums[R]:
                R -= 1
            else:
                L += 1
        
        return -1
    