class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        # base case:
        if s1 == s2:
            return True
        
        # find first and second difference between strings
        p1 = -1
        p2 = -1
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                p1 = i
                break
            
        for i in range(p1+1,len(s1)):
            if s1[i] != s2[i]:
                p2 = i
                break
         
        if p2 == -1:
            # return False if only one difference between strings
            return False
        else:
            # make swap
            t1 = s1[:p1] + s1[p2] + s1[p1+1:p2] + s1[p1] + s1[p2+1:]
            # Return true if both strings are equal after swap
            # Otherwise, return false
            return t1 == s2
        