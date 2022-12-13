class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 1
        while right < n:
            if nums[left] != nums[right]:
                left += 1
                right += 1
            else:
                del nums[right]
                n = len(nums)
