class Solution:
    def minimizedStringLength(self, s: str) -> int:
        letters = set()
        
        for c in s:
            letters.add(c)
        
        return len(letters)
    