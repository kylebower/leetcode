class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # sort nums in descending order
        nums.sort(key = lambda x: -x)
        
        # compute total sum
        total = sum(nums)
        
        # find Minimum Subsequence whose sum of elements is 
        # strictly greater than the sum of the non included elements
        k = 0
        sumSoFar = 0
        while sumSoFar <= total - sumSoFar:
            sumSoFar += nums[k]
            k += 1
        
        # return Minimum Subsequence in Non-Increasing Order
        return nums[:k]
    
    # time complexity: O(nlog(n))
    # space complexity: O(1)
    