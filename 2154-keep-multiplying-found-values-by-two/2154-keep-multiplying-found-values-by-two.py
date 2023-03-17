class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # make set of numbers in nums
        set_nums = set()
        for n in nums:
            set_nums.add(n)
        
        while original in set_nums:
            original *= 2
            
        return original
    