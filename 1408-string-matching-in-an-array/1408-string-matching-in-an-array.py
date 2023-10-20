class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # define result
        res = []
        
        # find substrings
        for i in range(len(words)):
            wi = words[i]
            for j in range(i+1,len(words)):
                wj = words[j]
                if self.isSubString(wi, wj):
                    res.append(wi)
                elif self.isSubString(wj, wi):
                    res.append(wj)
        
        # remove duplicates from res
        res = set(res)
        
        # return all strings in words that is a substring of another word
        return res
    
    def isSubString(self, w1, w2):
        # return True if w1 is a substring of w2
        if len(w1) > len(w2):
            return False
        else:
            for k in range(len(w2) - len(w1) + 1):
                if w1 == w2[k:k+len(w1)]:
                    return True
        return False