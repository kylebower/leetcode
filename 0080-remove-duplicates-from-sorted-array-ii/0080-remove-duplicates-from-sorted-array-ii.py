class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        # Base case
        if n < 2:
            return n
        
        # define pointers
        L = 0
        R = 1
        
        # remove duplicates 
        while R < len(nums):
            if nums[L] != nums[R]:
                L += 1
                R += 1
            elif R == L+1:
                R += 1
            else:
                del(nums[R])
        
        return len(nums)