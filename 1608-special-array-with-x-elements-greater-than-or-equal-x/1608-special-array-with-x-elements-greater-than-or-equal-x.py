class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # sort nums in descending order
        nums = sorted(nums, reverse = True)
        
        # define pointers
        n = len(nums)
        L = 1
        R = n
        
        # perform binary search to find if nums is special
        while L+1 < R:
            x = int(L+ (R-L)/2)
            if nums[x-1] >= x and nums[x] < x:
                return x
            elif nums[x-1] < x:
                R = x
            else:
                L = x                
        
        # Return x if the array is special, otherwise, return -1
        
        if L <= n-1 and nums[L-1] >= L and nums[L] < L:
            return L
        elif nums[R-1] >= R:
            return R
        else:
            return -1
    