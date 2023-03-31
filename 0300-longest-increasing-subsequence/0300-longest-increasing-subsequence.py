class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # base case        
        n = len(nums)
        if n < 2:
            return n
        
        # dynamic programming
        # dp[i] is the longest increasing subsequence of nums[0..i] 
        # which has nums[i] as the end element of the subsequence        
        dp = [1]*n
        
        # iterate to update dp[i]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)            
            
        # return longest strictly increasing subsequence
        return max(dp)