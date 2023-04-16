class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        # define dicts of char in s and t
        ds = {}
        dt = {}
        
        # populate dt and ds
        for c in s:
            ds[c] = ds.get(c,0) + 1
        for c in t:
            dt[c] = dt.get(c,0) + 1
            
        # count number of steps to make s and t anagrams
        res = 0
        for c in list(ds.keys()):
            if c in list(dt.keys()):
                res += abs(ds[c]-dt[c])
            else:  # c not in dt
                res += ds[c]
        for c in list(dt.keys()):
            if c not in list(ds.keys()):
                res += dt[c]
                
        # return result
        return res
            