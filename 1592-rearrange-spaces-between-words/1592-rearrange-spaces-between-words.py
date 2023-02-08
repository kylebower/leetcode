class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        nWords = len(words)
        nSpaces = text.count(' ')
        
        gap = 0 if nWords < 2 else nSpaces // (nWords - 1)
        end_space = nSpaces - gap * (nWords - 1)
        
        return (" " * gap).join(words) + (" " * end_space)
        