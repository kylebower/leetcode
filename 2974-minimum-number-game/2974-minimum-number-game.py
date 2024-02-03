class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for k in range(len(nums)//2):
            temp = nums[2*k]
            nums[2*k] = nums[2*k+1]
            nums[2*k+1] = temp
        return nums
    