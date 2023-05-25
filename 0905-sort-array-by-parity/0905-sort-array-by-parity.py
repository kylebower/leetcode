class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # short answer
        # nums.sort(key = lambda x: x%2)
        # return nums
        
        # two pointer solution
        # define two pointers
        L = 0
        R = 0
        
        # base case
        n = len(nums)
        if n < 2:
            return nums
        
        # move even to beginning
        while R < n:
            # find next odd number
            while L<n and nums[L]%2 == 0:
                L += 1
            # find next even number
            R = L + 1
            while R<n and nums[R]%2 == 1:
                R += 1
            # swap two numbers
            if R<n:
                temp = nums[R]
                nums[R] = nums[L]
                nums[L] = temp
                L += 1
        
        # return sorted array
        return nums