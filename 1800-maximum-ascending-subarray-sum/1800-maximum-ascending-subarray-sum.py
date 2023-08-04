class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:        
        # base case
        n = len(nums)
        if n < 2:
            return nums[0]
        
        # define pointers
        L = 0
        R = 1
        
        # increment sliding window
        cur = nums[0]
        res = cur
        while R < n:
            if nums[R] > nums[R-1]:
                cur += nums[R]
                # update max ascending subarray sum
                res = max(res, cur)
                # increment right pointer
                R += 1
            else:
                L = R
                cur = nums[L]
                # update max ascending subarray sum
                res = max(res, cur)
                R = L + 1
        
        # return maximum possible sum of an ascending subarray in nums
        return res
    