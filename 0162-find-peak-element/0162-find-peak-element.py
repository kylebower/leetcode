class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # base case
        n = len(nums)
        if n == 1:
            return 0
        
        # define pointers
        L = 0
        R = n-1
        mid = 0
        
        # perform binary search
        while L < R:
            # define midpoint
            mid = int(L + (R-L)/2)
            
            if nums[mid] < nums[mid+1]:
                L = mid + 1
            else:
                R = mid
        
        # return the index to any of the peaks
        return L