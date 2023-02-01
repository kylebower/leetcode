class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # sort nums
        nums.sort()
        
        # define two pointers
        n = len(nums)
        L = 0
        R = n-1
        
        # iterate to find first and last occurance of target
        # find first occurance
        while L + 1 < R:
            mid = int(L+(R-L)/2)
            if nums[mid] < target:
                L = mid+1
            elif nums[mid] > target:
                R = mid
            else:
                R = mid
        if nums[L] == target:
            first_target = L
        elif nums[R] == target:
            first_target = R
        else:
            return []
        
        # find last occurance
        L = 0
        R = n-1
        while L + 1 < R:
            mid = int(L+(R-L)/2)
            if nums[mid] > target:
                R = mid-1
            elif nums[mid] < target:
                L = mid
            else:
                L = mid
        if nums[R] == target:
            last_target = R
        elif nums[L] == target:
            last_target = L
        else:
            return []        
        
        # Return a list of the target indices of nums after sorting nums in non-decreasing order
        return range(first_target,last_target+1)
        