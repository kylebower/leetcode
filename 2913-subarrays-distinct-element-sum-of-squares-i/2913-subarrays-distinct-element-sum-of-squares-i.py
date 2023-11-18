class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in range(n):
            d = dict()
            for j in range(i,n):
                d[nums[j]] = d.get(nums[j],0)+1
                distinct_counts = sum([x==1 for x in list(d.values())])**2
                res += len(list(d.values()))**2
                
        return res
    