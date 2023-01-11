class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        n = len(nums)
        # define two pointers
        L = 0
        R = n-1
        if nums[R] < 0 or nums[L] > 0:
            return n
        
        # iterate to find rightmost negative number        
        while L + 1 < R:
            mid = int((L+R)/2)
            if nums[mid] >= 0:
                R = mid
            else:
                L = mid
        if nums[L] < 0:
            neg = len(nums[:L+1])
        else:
            neg = len(nums[:L])
            
        # define two pointers
        L = 0
        R = n-1
        
        # iterate to find leftmost positive number        
        while L + 1 < R:
            mid = int((L+R)/2)
            if nums[mid] <= 0:
                L = mid
            else:
                R = mid
        if nums[R] > 0:
            pos = len(nums[R:n])
        else:
            pos = len(nums[R+1:n])
        
        # return the maximum between the number of positive integers 
        # and the number of negative integers
        return max(pos,neg)
