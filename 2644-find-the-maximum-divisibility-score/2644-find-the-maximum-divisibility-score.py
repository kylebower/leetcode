class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        n = len(nums)
        mds = -1
        res = 0
        for d in divisors:
            cur = 0
            for num in nums:
                if num % d == 0:
                    cur += 1
            if cur > mds:
                mds = cur
                res = d
            elif cur == mds:
                res = min(d,res)
        return res
    