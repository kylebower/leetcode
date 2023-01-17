class Solution:
    def toLowerCase(self, s: str) -> str:
        res =""
        while s:
            res += s[0].lower()
            s = s[1:]
        
        return res