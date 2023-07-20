class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # define count of number of strings in words that are a prefix of s
        count = 0
        
        # count number of prefixes
        for w in words:
            if self.isPrefix(w, s):
                count += 1
                
        # return number of prefixes
        return count
    
    def isPrefix(self, w: str, s: str) -> bool:
        # define lengths of w and s
        nw = len(w)
        ns = len(s)
        
        # base case:
        if nw > ns:
            return False
        
        # return True if w is a prefix of s, else False
        return w == s[:nw]
    