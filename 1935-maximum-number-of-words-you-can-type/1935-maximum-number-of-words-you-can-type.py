class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        res = 0
        
        for w in text.split(' '):
            new_word = True
            d = {}
            for c in w:
                d[c] = d.get(c,0) + 1
            for c in brokenLetters:
                if c in d.keys():
                    new_word = False
            if new_word:
                res += 1
        
        return res
            