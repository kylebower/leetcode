class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n,0)+1
        
        ans = 0
        for k in d:
            if k+1 in d:
                ans = max(ans,d[k]+d[k+1])
        
        return ans
        