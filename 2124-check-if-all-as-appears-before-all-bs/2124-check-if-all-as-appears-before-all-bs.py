class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' not in s:
            return True
        
        index_b = s.index('b')
        return 'a' not in s[index_b:]