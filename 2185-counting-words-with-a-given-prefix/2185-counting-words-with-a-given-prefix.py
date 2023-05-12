class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # define count of number of words that have given prefix
        count = 0
        # count number of words that have given prefix
        for w in words:
            if self.hasPrefix(w,pref):
                count += 1
        # return count of number of words that have given prefix
        return count
    
    def hasPrefix(self, word: str, pref: str) -> bool:
        # return True if pref is a prefix for word
        nw = len(word)
        np = len(pref)
        if np > nw:
            return False
        else:
            return pref == word[:np]
        