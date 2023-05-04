class Solution:
    def arrangeCoins(self, n: int) -> int:
        # perform binary search
        L = 0
        R = n
        while L+1 < R:
            m = int(L + (R-L)/2)
            cur = int(m*(m+1)/2)
            if cur == n:
                return m
            elif cur < n:
                L = m
            else:  # cur > n
                R = m
                
        # return largest int m such that m(m+1)/2 <= n
        if R*(R+1)/2 <= n:
            return R
        else:
            return L
        
    # time complexity: O(log(n))
    # space complexity: O(1)
        