class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                
        # shift 0's to the end of the array
        count0 = 0
        for i in range(n):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = 0
                nums[i-count0] = temp
            else:
                count0 += 1
        return nums
            