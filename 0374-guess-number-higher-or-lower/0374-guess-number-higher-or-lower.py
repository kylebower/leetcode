# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # define two pointers
        L = 1
        R = n
        
        # perform binary search to find number
        while L + 1 < R:
            mid = math.ceil((L+R)/2)
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                R = mid
            else:
                L = mid
        
        # return number
        if guess(L) == 0:
            return L
        else:
            return R
        
        # time complexity: O(logn)
        # space complexity: O(1)
