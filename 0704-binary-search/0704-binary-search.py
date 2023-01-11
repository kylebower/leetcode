class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # define pointers
        n = len(nums)
        L = 0
        R = n-1
        
        # perform binary search to find target
        while L + 1 < R:
            mid = int((L+R)/2)
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess < target:
                L = mid
            else:
                R = mid
            
        # If target exists, then return its index. 
        # Otherwise, return -1
        if nums[L] == target:
            return L
        elif nums[R] == target:
            return R
        else:
            return -1
        
        # time complexity: O(logn)
        # space complexity: O(1)
