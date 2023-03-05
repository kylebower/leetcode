class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_nums = min(nums)
        max_nums = max(nums)
        
        gcd = 1
        k = 1
        for k in range(1,min_nums+1):
            if min_nums%k == 0 and max_nums%k == 0:
                gcd = k
        
        return gcd