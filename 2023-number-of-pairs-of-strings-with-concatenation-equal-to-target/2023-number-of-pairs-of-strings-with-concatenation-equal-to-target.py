class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    if int(str(nums[i]) + str(nums[j])) == int(target):
                        res += 1
        return res
    