class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = math.inf
        for num in nums:
            if abs(num) < abs(res):
                res = num
            elif abs(num) == abs(res) and num > res:
                res = num
        return res
        