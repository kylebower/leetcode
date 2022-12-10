class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        i = 0
        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i = i+1
