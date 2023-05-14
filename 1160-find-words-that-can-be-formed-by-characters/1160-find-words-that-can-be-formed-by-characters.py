class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        count = 0
        for w in words:
            d = {}
            for c in chars:
                d[c] = d.get(c,0)+1
                
            if self.isGoodWord(w,d):
                count += len(w)
        
        return count
    
    def isGoodWord(self, word: str, dw: dict) -> bool:
        for c in word:
            if dw.get(c,0) == 0:
                return False
            dw[c] = dw.get(c,0)-1
        return True
        