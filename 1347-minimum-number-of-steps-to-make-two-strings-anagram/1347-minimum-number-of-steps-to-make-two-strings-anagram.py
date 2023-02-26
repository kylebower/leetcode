class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        # define dict for s and t
        ds = {}
        dt = {}
        
        # fill dicts
        for c in s:
            ds[c] = ds.get(c,0) + 1
        for c in t:
            dt[c] = dt.get(c,0) + 1
            
        # base case
        nSteps = 0
        if ds == dt:
            return nSteps
        
        # iterate to count min number of steps
        for key in list(ds.keys()):
            nSteps += max(0, ds.get(key) - dt.get(key,0))
        
        # Return the minimum number of steps to make t an anagram of s
        return nSteps
    