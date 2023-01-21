class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # define dictionaries of char in s and t
        ds = {}
        dt = {}
        
        # populate dictionaries
        for c in s:
            ds[c] = ds.get(c,0) + 1
        for c in t:
            dt[c] = dt.get(c,0) + 1
        
        # return true if t is an anagram of s, and false otherwise
        return ds == dt
