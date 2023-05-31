class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # sort nums
        nums.sort()
        
        # find min diff between Highest and Lowest of K Scores
        n = len(nums)
        min_diff = math.inf
        for i in range(n-k+1):
            cur_diff = nums[i+k-1] - nums[i]
            min_diff = min(min_diff, cur_diff)
        
        # return min diff
        return min_diff
        