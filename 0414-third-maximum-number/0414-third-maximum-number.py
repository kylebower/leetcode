class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = sorted(set(nums), reverse = True)
        if len(distinct) >= 3:
            return distinct[2]
        else:
            return distinct[0]
        