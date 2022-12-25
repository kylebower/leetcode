class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # define pointers
        n = len(nums)
        L, R = 0, n-1
        
        # base case
        if nums[L] <= nums[R]:
            return nums[L]
        
        # perform binary search
        while L + 1 < R:
            mid = int( L + (R - L) / 2)
            if nums[mid] < nums[R]:
                R = mid
            else:
                L = mid
        
        # return minimum element of array
        return min(nums[L], nums[R])
    
    # time complexity: O(log n)
    # space complexity: O(1)
