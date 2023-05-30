class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # base case
        n = len(nums)
        if n < 2:
            return nums
        
        # sort odd indices of nums in non-increasing order
        nums[1::2] = sorted(nums[1::2], key = lambda x: -x)
        
        # sort even indices of nums in non-decreasing orde
        nums[0::2] = sorted(nums[0::2])
        
        # Return the array formed after rearranging the values of nums
        return nums
    