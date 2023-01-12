class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # define lengths of strings s and t
        ns = len(s)
        nt = len(t)
        
        # handle base cases
        if ns == 0:
            return True
        elif nt == 0:
            return False
        
        # check if s is a subsequence of t
        ti = 0
        for si in range(ns):
            if ti == nt:
                return False
            while s[si] != t[ti]:
                ti += 1
                if ti == nt:
                    return False
            ti += 1
                
        # return true if s is a subsequence of t        
        return True
        