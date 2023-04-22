class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # define dict of count of each word in words1 and words2
        d1 = {}
        d2 = {}
        for w in words1:
            d1[w] = d1.get(w,0)+1
        for w in words2:
            d2[w] = d2.get(w,0)+1
        
        # count number of strings that appear exactly once in each of the two arrays
        count = 0
        for w in words1:
            if d1[w] == 1 and d2.get(w,0) == 1:
                count += 1
        
        # return count
        return count
    