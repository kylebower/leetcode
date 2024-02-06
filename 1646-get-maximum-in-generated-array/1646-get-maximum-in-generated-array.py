class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        
        nums = [0]*(n+1)
        nums[1] = 1
        
        for k in range(2,n+1):
            if k%2 == 0:
                nums[k] = nums[k//2]
            else:
                nums[k] = nums[k//2] + nums[k//2 + 1]
        
        return max(nums)
    