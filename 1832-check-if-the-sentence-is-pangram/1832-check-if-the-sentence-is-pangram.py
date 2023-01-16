class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for c in sentence:
            d[c] = 1
        
        return len(list(d.values())) == 26
