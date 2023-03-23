class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        
        res = self.computeProductDifference((nums[n-1], nums[n-2]), (nums[0], nums[1]))        
        
        return res
    
    def computeProductDifference(self, p1, p2):
        (a,b) = p1
        (c,d) = p2
        return (a * b) - (c * d)