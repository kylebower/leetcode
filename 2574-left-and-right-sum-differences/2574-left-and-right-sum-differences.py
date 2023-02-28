class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        # define left and right sum
        n = len(nums)
        leftSum = [0]*n
        rightSum = [0]*n
        
        # iterate to compute left and right sum
        for i in range(1,n):
            leftSum[i] = leftSum[i-1] + nums[i-1]
            j = n-i
            rightSum[j-1] = rightSum[j] + nums[j]
        # compute result
        res = [0]*n
        for i in range(n):
            res[i] = abs(leftSum[i] - rightSum[i])
        
        # return result
        return res
    