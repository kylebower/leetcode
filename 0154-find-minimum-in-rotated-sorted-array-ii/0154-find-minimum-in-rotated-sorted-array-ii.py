class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # define pointers
        n = len(nums)
        L, R = 0, n-1
        
        # base case
        if nums[L] < nums[R]:
            return nums[L]
        
        # perform binary search to find min element
        while L + 1 < R:
            mid = int(L + (R - L)/2)
            if nums[mid] < nums[R]:
                R = mid
            elif nums[mid] == nums[R]:
                R -= 1
            else:
                L = mid
        
        # return minimum element in array
        return min(nums[L], nums[R])