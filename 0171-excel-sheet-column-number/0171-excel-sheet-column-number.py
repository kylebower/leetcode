class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        
        num_of_char = 0
        for c in self.reverse(columnTitle):
            res += self.char_to_int(c)*26**num_of_char                
            num_of_char += 1
        
        return res
        
    def char_to_int(self, c):
        return ord(c)-64
    
    def reverse(self, s):
        res = ""
        while s:
            res += s[-1]
            s = s[:-1]
        return res