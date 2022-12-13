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
        index1 = 0
        index2 = 1
        
        # loop
        while index2 <= n-1:
            if nums[index1] != 0:
                index1 += 1
                index2 += 1
            else:
                while nums[index2] == 0 and index2 < n-1:
                    index2 += 1
                if nums[index2] != 0:
                    num1 = nums[index1]
                    num2 = nums[index2]
                    nums[index1] = num2
                    nums[index2] = num1
                    index1 += 1
                    index2 += 1
                else:
                    return
        return
    