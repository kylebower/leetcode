class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # define variables
        n = len(nums)
        res = -1
        
        # iterate to find max sum of a pair of numbers from nums such that the maximum digit in both numbers are equal
        for i in range(n):
            maxDigitI = max([int(c) for c in str(nums[i])])
            for j in range(i+1,n):
                maxDigitJ = max([int(c) for c in str(nums[j])])
                if maxDigitI == maxDigitJ:
                    res = max(res, nums[i] + nums[j])        
        
        # return result
        return res
    
    # time complexity: O(n^2)
    # space complexity: O(1)
    