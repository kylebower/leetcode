class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        # base case
        if n < 1:
            return [-1,-1]
        
        # define pointers
        L, R = 0, n-1
        
        # perform binary search to find indices
        while L <= R:
            # return indices of target if found
            if nums[L] == target and nums[R] == target:
                return [L,R]
            
            mid = int((L+R)/2)
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            elif nums[L] == target:
                R -= 1
            else:
                L += 1
            
        # return starting and ending position of a given target value.
        # If target is not found in the array, return [-1, -1].
        return [-1,-1]
