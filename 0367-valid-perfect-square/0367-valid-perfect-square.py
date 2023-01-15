class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # base case:
        if num == 1:
            return True
        
        # define pointers
        low = 1
        high = num
        
        # iterate to find sqrt
        while low + 1 < high:
            mid = int((low+high)/2)
            if mid*mid == num:
                return True
            elif mid*mid < num:
                low = mid
            else:
                high = mid
                
        return False
