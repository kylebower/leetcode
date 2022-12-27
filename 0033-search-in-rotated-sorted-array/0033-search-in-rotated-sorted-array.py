class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # base case
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                result = 0
            else:
                result = -1
            return result
        
        # define pointers
        L, R = 0, n-1
        
        # perform binary search
        if nums[L] > target and nums[R] < target:
            return -1
        
        if nums[L] == target:
            return L
        elif nums[R] == target:
            return R
            
        while L < R:
            mid = int(L + (R-L)/2)
            if nums[mid] == target:
                return mid
            elif nums[L] == target:
                return L
            elif nums[R] == target:
                return R
            # print("L: " + str(L))
            # print("R: " + str(R))
            # print("mid: " + str(mid))
            
            if nums[L] < nums[mid]:
                if nums[L] <= target and target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target and target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
            
            
            # if nums[L] < target and target < nums[mid]:
            #     R = mid
            # elif nums[mid] < target and target < nums[R]:
            #     L = mid
            # elif nums[mid] > target and target < nums[R]:
            #     L = mid
            # elif nums[L] < target and target > nums[mid]:
            #     R = mid
            # else:
            #     L += 1
            # if (nums[R] > target and nums[mid] < target) or (nums[R] > target and nums[mid] > nums[R]):
            #     L = mid
            # elif (nums[mid] > target and nums[L] < target) or (nums[L] < target and nums[mid] < nums[L]):
            #     R = mid
            # else:
            #     return mid
        
        # return index of target if it is in nums, or -1 if it is not in nums
        # if nums[L] == target:
        #     result = L
        # elif nums[R] == target:
        #     result = R
        # else:
        #     result = -1
        # return result
        return -1