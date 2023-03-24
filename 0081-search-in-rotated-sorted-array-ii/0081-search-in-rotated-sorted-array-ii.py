class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # perform binary search to find pivot index
        n = len(nums)
        L, R = 0, n-1
        while L + 1 < R:
            while nums[L] == nums[R] and L+1 < R:
                R -= 1
            mid = int(L + (R-L)/2)
            if nums[mid] >= nums[L]:
                L = mid
            else:
                R = mid
        
        if nums[R] >= nums[L]:
            pivot = R
        else:
            pivot = L
        
        # perform binary search to check if target is in nums
        if nums[0] <= target:
            L = 0
            R = pivot
        else:
            L = min(pivot+1,n-1)
            R = n-1
        
        while L + 1 < R:
            mid = int(L + (R-L)/2)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                L = mid
            else:
                R = mid
        
        # return true if target is in nums, or false if it is not in nums
        return nums[L] == target or nums[R] == target
            
    # time complexity: O(log(n))
    # space complexity: O(1)    
    