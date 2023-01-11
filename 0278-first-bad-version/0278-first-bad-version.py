# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # define pointers
        L = 1
        R = n
        
        # binary search to find first bad version
        while L + 1 < R:
            mid = int((L+R)/2)
            if isBadVersion(mid):
                R = mid
            else:
                L = mid
        
        # return first bad version
        if isBadVersion(L):
            return L
        else:
            return R

        # time complexity: O(logn)
        # space complexity: O(1)
