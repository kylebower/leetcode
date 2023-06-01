class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0]+nums[-1]
        
        for k in range(n//2):
            cur = nums[k]+nums[n-k-1]
            res = max(res,cur)
            
        return res
        