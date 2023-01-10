import math
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # base cases
        n = len(nums)
        if target <= nums[0]:
            return 0
        elif target > nums[n-1]:
            return n
        
        # define pointers
        L = 0
        R = n-1
        
        # perform binary search
        while L + 1 < R:
            mid = int( (L+R)/2 )
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid
            else:
                R = mid
                
        # return the index if the target is found. 
        # If not, return the index where it would be if it were inserted in order
        if target <= nums[L]:
            return L
        elif target <= nums[R]:
            return R
        else:
            return R+1

        # time complexity: O(log n)
        # space complexity: O(1)
