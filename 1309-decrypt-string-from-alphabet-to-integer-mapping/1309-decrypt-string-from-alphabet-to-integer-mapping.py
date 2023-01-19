class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2]=='#':
                c = chr(int(s[i:i+2])+96) # chr(97-122) is 'a' to 'z'
                i += 3
            else:
                c = chr(int(s[i])+96)
                i += 1
            res.append(c)
        
        return "".join(res)
