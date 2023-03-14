class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # define output array
        res = []
        
        # use input array itself as a hash to store which numbers have been seen before (by making them negative)
        for n in nums:
            if nums[abs(n)-1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
        
        return res
    