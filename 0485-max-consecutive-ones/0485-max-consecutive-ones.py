class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        n = len(nums)
        # define sliding window pointers
        L = 0
        R = 0
        
        # iterate to find maximum number of consecutive 1's
        while R < n:
            while R < n and nums[R] == 1:
                R += 1
            if R - L > max_consecutive_ones:
                max_consecutive_ones = R - L
            L = R + 1
            R = L
            
        # return the maximum number of consecutive 1's in the array
        return max_consecutive_ones
