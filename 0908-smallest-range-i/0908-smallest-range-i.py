class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # define variables
        n = len(nums)
        
        # find max and min in nums
        maxNums = max(nums)
        minNums = min(nums)
        
        # find minimum score of nums after applying the operations
        bestScore = max(maxNums - minNums - 2*k, 0)
        
        # return result
        return bestScore
    
    # time complexity: O(n)
    # space complexity: O(1)
        