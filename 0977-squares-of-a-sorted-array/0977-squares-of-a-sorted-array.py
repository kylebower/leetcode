class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Base case
        if n < 2:
            for i in range(n):
                nums[i] = nums[i] ** 2
            return nums
        
        # define pointers
        R = 0
        while R < n and nums[R] < 0:
            R +=1
        L = R - 1
        
        # sort
        sorted_nums = [None]*n
        for i in range(n):
            if L < 0 or R < n and nums[R] < -nums[L] :
                sorted_nums[i] = nums[R]
                R += 1
            else:
                sorted_nums[i] = nums[L]
                L -= 1                
        
        # square each element
        for i in range(n):
            sorted_nums[i] = sorted_nums[i] ** 2
        
        # return array
        return sorted_nums
    
        # time complexity O(n)
        # space complexity O(1)
        