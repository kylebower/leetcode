class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        n = len(nums)       # number rows
        m = len(nums[0])    # number cols
        
        # sort each row in the matrix
        for i,row in enumerate(nums):
            nums[i] = sorted(row)
        
        # compute score
        for mi in range(m):
            cur = 0
            for ni in range(n):
                cur = max(cur, nums[ni][mi])            
            score += cur
        
        # Return the final score
        return score
    