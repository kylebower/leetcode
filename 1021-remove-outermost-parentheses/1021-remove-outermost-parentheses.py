class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        countL = 0
        countR = 0
        start = 0
        for i, c in enumerate(s):
            if c == '(':
                countL += 1
            else:
                countR += 1
            
            if countL == countR:
                res += s[start+1:i]
                countL = 0
                countR = 0
                start = i+1
                
        return res
                