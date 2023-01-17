class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # define dictionaries of characters in strings s and t
        ds = {}
        dt = {}
        
        # populate dictionaries
        for c in s:
            ds[c] = ds.get(c,0)+1
        for c in t:
            dt[c] = dt.get(c,0)+1
        
        # return letter added
        for c in dt:
            if not c in ds:
                return c
        
        for c in ds:
            if ds[c] != dt[c]:
                return c
