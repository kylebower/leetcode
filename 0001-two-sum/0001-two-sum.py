class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sorted_nums = [None]*n
        for i in range(n):
            sorted_nums[i] = nums[i]
        sorted_nums.sort()
        
        # define pointers
        L = 0
        R = n-1
        
        # iterate to find indices
        while L < R:
            current_sum = sorted_nums[L] + sorted_nums[R]
            if current_sum == target:
                break
            elif current_sum < target:
                L += 1
            else:
                R -= 1
        
        left = 0
        while nums[left] != sorted_nums[L]:
            left += 1
        right = 0
        while nums[right] != sorted_nums[R] or right == left:
            right += 1
        # return indices of the two numbers such that they add up to target
        return [left, right]
        