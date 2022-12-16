class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        # create sorted array of nums
        sorted_nums = []
        for i, x in enumerate(nums):
            sorted_nums.append([x, i])
        sorted_nums.sort()
        
        # define pointers
        L = 0
        R = n-1
        
        # iterate to find indices
        while L < R:
            current_sum = sorted_nums[L][0] + sorted_nums[R][0]
            if current_sum == target:
                return [sorted_nums[L][1], sorted_nums[R][1]]
            elif current_sum < target:
                L += 1
            else:
                R -= 1
        