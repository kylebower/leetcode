class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case
        n1 = len(s1)
        n2 = len(s2)
        result = False
        if n2 < n1:
            return result
        
        # define dictionary of characters in s1
        s1_dict = {}
        for x in s1:
            s1_dict.update({x:s1_dict.get(x,0)+1})
        
        # define pointers
        L = 0
        R = 0
        
        # iterate sliding window to find result
        sw_dict = {}
        while R < n2:
            # expand window
            sw_dict.update({s2[R]:sw_dict.get(s2[R],0)+1})
            
            # contract window
            if R - L + 1 > n1:
                sw_dict.update({s2[L]:sw_dict.get(s2[L],0)-1})
                if sw_dict.get(s2[L],0) == 0:
                    del sw_dict[s2[L]]
                L += 1
            
            if sw_dict == s1_dict:
                return True
            
            R += 1
        
        # return true if s2 contains a permutation of s1, or false otherwise.
        return result
