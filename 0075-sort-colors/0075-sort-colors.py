class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n < 2:
            return
        
        # define pointers
        W = 0 # first W
        B = 0 # first B
        
        # sort array in-place so that objects of the same color are adjacent,
        # with the colors in the order red, white, and blue
        for i in range(n):
            if nums[i] == 0:
                nums[i] = 2
                nums[B] = 1
                nums[W] = 0
                B += 1
                W += 1
            elif nums[i] == 1:
                nums[i] = 2
                nums[B] = 1
                B += 1
        # time complexity: O(n)
        # space complexity: O(1)
