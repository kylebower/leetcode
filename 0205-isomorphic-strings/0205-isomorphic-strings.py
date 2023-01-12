class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        n = len(s)
        
        # define dict of occurances of each letter in s and t
        ds = {}
        dt = {}
        
        for i in range(n):
            ds[s[i]] = ds.get(s[i],[]) + [i]
            dt[t[i]] = dt.get(t[i],[]) + [i]
        
        # return true if s and t are isomorphic, otherwise return false
        return list(ds.values()) == list(dt.values())
    
    # time complexity: O(n)
    # space complexity: O(n)
