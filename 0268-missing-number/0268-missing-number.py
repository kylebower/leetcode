class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # sort nums
        nums.sort()
        
        # find missing number
        n = len(nums)
        if nums[0] != 0:
            return 0
        for i in range(n-1):
            if nums[i] != nums[i+1]-1:
                return i+1
        
        return n
