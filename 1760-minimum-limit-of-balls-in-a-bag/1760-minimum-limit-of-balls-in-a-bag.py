class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        L = 1
        R = max(nums)
        # perform binary search to find max size of a bag
        while L+1 < R:
            mid = int(L+(R-L)/2)
            if self.nBags(mid, nums) <= n + maxOperations:
                R = mid
            else:
                L = mid
        
        if self.nBags(R, nums) <= n + maxOperations:
            maxSize = R
        else:
            maxSize = L
        
        return maxSize
    
    def nBags(self, maxSize: int, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += ceil(num / maxSize)
        return res
        
        