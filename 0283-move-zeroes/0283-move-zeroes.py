class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # base case
        n = len(nums)
        if n < 2:
            return
        
        # define pointers
        left = 0
        right = 1
        
        # loop
        while right < n:            
            if nums[left] != 0:
                left += 1
                right += 1
            elif nums[right] == 0:
                right += 1
            else:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
        return
    