class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        n = len(s)
        # base case
        if n < 3:
            return 0
        
        # add first three char to dict d
        d = {}
        for i in range(3):
            c = s[i]
            d[c] = d.get(c,0)+1
        
        # define count of good substrings
        result = 0
        if len(list(d.keys())) == 3:
            result += 1
        
        # move sliding window to count all good substrings
        for i in range(n-3):
            # remove leftmost char
            L_char = s[i]
            d[L_char] = d.get(L_char) - 1
            if d[L_char] == 0:
                d.pop(L_char)
            
            # add new char
            new_char = s[i+3]
            d[new_char] = d.get(new_char,0)+1
            
            # update count of good strings
            if len(list(d.keys())) == 3:
                result += 1
                
        # return number of good substrings
        return result
