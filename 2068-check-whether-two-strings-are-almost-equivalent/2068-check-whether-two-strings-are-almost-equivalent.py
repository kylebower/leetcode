class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # make frequency counts of letters in each word
        d1 = collections.Counter(word1)
        d2 = collections.Counter(word2)
        
        # return False if differences between the frequencies of a letter is > 3
        for c in d1:
            if abs(d1[c]-d2[c]) > 3:
                return False
        for c in d2:
            if abs(d1[c]-d2[c]) > 3:
                    return False
        
        # return True if number of differences is at most 3
        return True
    