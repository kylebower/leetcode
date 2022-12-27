class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # base case
        n = len(nums)
        # if n == 1:
        #     if nums[0] == target:
        #         result = 0
        #     else:
        #         result = -1
        #     return result
        
        # define pointers
        L, R = 0, n-1
        
        # perform binary search
#         if nums[L] > target and nums[R] < target:
#             return -1
        
#         if nums[L] == target:
#             return L
#         elif nums[R] == target:
#             return R
            
        while L <= R:
            mid = int(L + (R-L)/2)
            if nums[mid] == target:
                return mid
            # elif nums[L] == target:
            #     return L
            # elif nums[R] == target:
            #     return R
            
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
