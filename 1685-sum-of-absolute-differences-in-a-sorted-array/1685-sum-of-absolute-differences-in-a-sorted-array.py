class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        
        preS = 0
        sufS = 0
        preSum = [0]*n
        sufSum = [0]*n
        
        for i in range(n):
            preSum[i] = preS
            sufSum[n-1-i] = sufS
            preS += nums[i]
            sufS += nums[n-1-i]
        
        for i in range(n):
            if i == 0:
                res[i] = sufSum[i]-(n-1)*nums[i]
            elif i == n-1:
                res[i] = (n-1)*nums[i] - preSum[i]
            else:
                res[i] = sufSum[i]-(n-1-i)*nums[i] + i*nums[i] - preSum[i]
        
        return res
    