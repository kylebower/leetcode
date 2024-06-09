class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        nWords = len(words)
        d = dict()
        
        for w in words:
            for c in w:
                d[c] = d.get(c,0) + 1
        
        for value in list(d.values()):
            if value % nWords != 0:
                return False
        
        return True
    