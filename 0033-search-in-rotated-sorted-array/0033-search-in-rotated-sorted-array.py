class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        # define pointers
        L, R = 0, n-1
        
        # perform binary search to find index of target
        while L <= R:
            mid = int((R+L)/2)
            if nums[mid] == target:
                return mid
            
            if nums[L] <= nums[mid]:
                if nums[L] <= target and target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target and target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        
        # return index of target if it is in nums, or -1 if it is not in nums
        return -1
    
    # time complexity: O(log n)
    # space complexity: O(1)
