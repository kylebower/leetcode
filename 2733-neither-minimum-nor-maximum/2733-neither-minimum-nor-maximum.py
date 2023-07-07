class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        # base case:
        if n < 3:
            return -1
        
        # return middle of first three numbers
        return sorted(nums[:3])[1]
    
    # time complexity: O(1)
    # space complexity: O(1)
    