class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort nums
        nums.sort()
                
        # base case
        n = len(nums)
        if n < 2:
            return n
                
        # iterate sliding window to find max freq
        L = 0
        result = 0
        for R in range(n):
            k += nums[R]
            if k < nums[R]*(R-L+1):
                k -= nums[L]
                L += 1
                
        # return max possible frequency
        return R-L+1
            