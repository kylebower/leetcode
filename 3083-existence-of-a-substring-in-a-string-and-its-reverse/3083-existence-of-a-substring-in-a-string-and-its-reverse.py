class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s2 = s[::-1]
        for k in range(len(s)-1):
            if s[k:k+2] in s2:
                return True
        return False
    