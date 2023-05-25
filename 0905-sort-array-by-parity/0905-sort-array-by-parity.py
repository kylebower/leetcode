class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # short answer
        # nums.sort(key = lambda x: x%2)
        # return nums
        
        # two pointer solution
        # define two pointers
        L = 0
        n = len(nums)
        R = n-1
        
        # base case
        if n < 2:
            return nums
        
        # use two pointers to move even to beginning
        while L < R:
            if nums[L]%2 == 0:
                # find odd
                L += 1
            elif nums[R]%2 == 1:
                # find even
                R -= 1
            else:
                # swap even and odd
                temp = nums[R]
                nums[R] = nums[L]
                nums[L] = temp
        
        # return sorted array
        return nums