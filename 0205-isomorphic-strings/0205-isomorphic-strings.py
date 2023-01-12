class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        n = len(s)
        
        # define dict of occurances of each letter in s and t
        ds = {}
        dt = {}
        
        for i in range(n):
            if s[i] in ds:
                ds[s[i]] = ds[s[i]] + [i]
            else:
                ds[s[i]] = [i]
            if t[i] in dt:
                dt[t[i]] = dt[t[i]] + [i]
            else:
                dt[t[i]] = [i]
        
        # return true if s and t are isomorphic, otherwise return false
        return list(ds.values()) == list(dt.values())
    
    # time complexity: O(n)
    # space complexity: O(n)
