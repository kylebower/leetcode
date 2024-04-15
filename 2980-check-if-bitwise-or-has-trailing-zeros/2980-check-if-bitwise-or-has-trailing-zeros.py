class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(n-1):
            for j in range(i+1,n):
                number = nums[i] | nums[j]
                if (number != 0) and (number % 2 == 0):
                    return True
        
        return False
    