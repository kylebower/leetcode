class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        # brute force check each substring
        n = len(s)
        # base case
        longest = ""
        if n < 2:
            return longest
        L = 0
        while L < n:
            R = L
            while R < n:
                cur = s[L:R+1]
                if len(cur) > len(longest) and self.isNice(cur):
                    longest = cur
                R += 1
            L += 1
        
        return longest
    
    def isNice(self, s: str) -> bool:
        # return True if s is a nice string, else False
        d = {}
        for c in s:
            d[c] = d.get(c,0)+1
        
        for c in d:
            if c.upper() not in d or c.lower() not in d:
                return False
        
        return True
            