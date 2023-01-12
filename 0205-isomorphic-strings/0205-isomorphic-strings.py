class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        n = len(s)
        
        # define dict of occurances of each letter in s and t
        ds = {}
        dt = {}
        
        for i, val in enumerate(s):
            ds[val] = ds.get(val,[]) + [i]
        for i, val in enumerate(t):
            dt[val] = dt.get(val,[]) + [i]
        
        # return true if s and t are isomorphic, otherwise return false
        return list(ds.values()) == list(dt.values())
    
    # time complexity: O(n)
    # space complexity: O(n)
