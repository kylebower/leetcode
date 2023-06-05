class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(x: int) -> int:
            # return power value of x
            if x == 1:
                return 0
            elif x%2==0:
                return 1 + power(x // 2)
            else:
                return 1 + power(3*x + 1)
        return sorted(range(lo, hi+1), key = lambda x: power(x))[k-1]
    