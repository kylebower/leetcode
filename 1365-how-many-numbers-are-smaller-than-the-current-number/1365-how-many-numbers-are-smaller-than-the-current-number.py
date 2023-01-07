class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [nan]*n
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    count += 1
            result[i] = count
        return result
        