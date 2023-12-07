class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        n = len(nums)
        
        # base case:
        if n < 2:
            return -1
        
        # find max value after index i in nums
        maxAfter = [-inf]*n
        maxAfter[-1] = -inf
        for i in range(n-1):
            j = n-2-i
            maxAfter[j] = max(maxAfter[j+1], nums[j+1])
        
        # compute result
        for i in range(n-1):
            if maxAfter[i] - nums[i] != 0:
                res = max(res, maxAfter[i] - nums[i])
        
        # return result
        return res
    
    # time complexity: O(n)
    # space complexity: O(n)
        