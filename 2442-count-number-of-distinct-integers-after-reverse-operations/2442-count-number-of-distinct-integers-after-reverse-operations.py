class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        n = len(nums)
        for i in range(n):
            nums.append(self.reverse(nums[i]))
        
        return len(set(nums))
    
    def reverse(self, m):
        res = 0
        while m > 0:
            res = res * 10 + m%10
            m //= 10
        return res
    