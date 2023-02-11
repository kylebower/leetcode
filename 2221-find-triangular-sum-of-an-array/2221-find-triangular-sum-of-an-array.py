class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # base case:
        n = len(nums)
        if n == 1:
            return nums[0]
        # new_nums = self.getNextRow(nums)
        new_nums = [(x+y)%10 for x,y in zip(nums[:n-1],nums[1:n])]
        return self.triangularSum(new_nums)
    
    def getNextRow(self, nums):
        n = len(nums)
        res = [0]*(n-1)
        for i in range(n-1):
            res[i] = (nums[i] + nums[i+1]) % 10
        return res
