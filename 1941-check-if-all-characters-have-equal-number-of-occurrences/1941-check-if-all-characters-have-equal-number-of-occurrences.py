class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # base case
        if len(s) < 2:
            return True
        
        # define dictionary of occurrences
        d = {}
        
        # update dictionary
        for c in s:
            d[c] = d.get(c,0) + 1
        
        # return true if all the characters that appear in s have the same number of occurrences
        freq = list(d.values())
        for f in freq:
            if f != freq[0]:
                return False            
        return True        
        