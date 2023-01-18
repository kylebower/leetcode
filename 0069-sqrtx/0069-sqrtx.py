class Solution:
    def mySqrt(self, x: int) -> int:
        # base case
        if x < 2:
            return x
                
        # define pointers
        L = 0
        R = x
        
        # perform binary search to find sqrt
        while L+1 < R:
            mid = int(L+(R-L)/2)
            sq = mid*mid
            if sq == x:
                return mid
            elif sq > x:
                R = mid
            else:
                L = mid
        
        # return sqrt of x rounded down to the nearest integer
        return L
