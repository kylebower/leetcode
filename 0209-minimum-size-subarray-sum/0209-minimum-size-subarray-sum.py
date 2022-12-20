class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # define pointers
        L = 0
        R = 0
        
        n = len(nums)
        result = math.inf
        curr_sum = 0
        
        # iterate and use sliding window to find minimal length subarray
        while R < n:
            curr_sum += nums[R]
            while target <= curr_sum:
                result = min(result, R - L + 1)
                curr_sum -= nums[L]
                L += 1
            R += 1
        
        # If there is no such subarray, return 0
        if result == math.inf:
            result = 0
        
        # return the minimal length of a subarray whose sum is greater than or equal to target
        return result
    
        # time complexity: O(n)
        # space complexity: O(1)
