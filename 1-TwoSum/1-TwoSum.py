# Last updated: 7/2/2025, 10:46:09 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = dict()
        for i in range(n):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i
        return []