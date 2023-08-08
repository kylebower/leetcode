class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # sort words by lexicographical order
        words.sort()
        
        # make dict of occurences of each word in words
        d = dict()
        for w in words:
            d[w] = d.get(w,0) + 1        
        
        # sort words by the frequency from highest to lowest
        res = sorted(list(d.keys()), key = lambda x: d[x], reverse = True)
        
        # return k most frequent strings
        return res[:k]
    