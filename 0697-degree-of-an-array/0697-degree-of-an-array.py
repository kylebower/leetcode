class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        d = {} # frequency
        e = {} # indices
        for i,n in enumerate(nums):
            d[n] = d.get(n,0)+1
            en = e.get(n,[])
            e[n] = en + [i]
        
        max_freq = max(list(d.values()))
        
        min_length = len(nums)
        for n in e:
            if d[n] == max_freq:
                min_length = min(min_length,e[n][-1]-e[n][0]+1)

        return min_length
        