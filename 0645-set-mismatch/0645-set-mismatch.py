class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # sort nums
        nums.sort()
        
        # iterate through nums to find repeat and missing number
        n = len(nums)
        if nums[0] != 1:
            missing = 1
            repeat = n
        else:
            repeat = 1
            missing = n
        L = 0
        R = 1
        while R < n:
            if nums[R] == nums[L]:
                repeat = nums[L]
            elif nums[R] == nums[L] + 2:
                missing = nums[L] + 1
            L += 1
            R += 1
        
        # repeat and missing number
        return [repeat, missing]
    
    # time complexity: O(nlog(n))
    # space complexity: O(1)