class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # base case
        n = len(nums)
        if n == 0:
            return []
        elif n == 1:
            return [str(nums[0])]
        
        res = []
        # define two pointers
        L = 0
        R = 0
        cur = nums[0]
        while R < n:
            while R < n and nums[R] <= cur+1:
                cur = nums[R]
                R += 1
            if cur == nums[L]:
                res.append(str(cur))
            else:
                res.append(str(nums[L]) + "->" + str(cur))
            L = R
            if R < n:
                cur = nums[R]
            
        return res
        