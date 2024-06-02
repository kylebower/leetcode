class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s2 = self.reverse(s)
        for k in range(len(s)-1):
            if s[k:k+2] in s2:
                return True
        return False
        
    def reverse(self, string: str) -> str:
        res = ''
        for c in string:
            res = c + res
        return res
    