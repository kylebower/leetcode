class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        n_pairs = 0
        n = len(nums)
        
        # base case
        if n < 2:
            return 0
        
        # iterate to count number of pairs
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(nums[i] - nums[j]) == k:
                    n_pairs += 1
        
        # return number of pairs With Absolute Difference K
        return n_pairs
