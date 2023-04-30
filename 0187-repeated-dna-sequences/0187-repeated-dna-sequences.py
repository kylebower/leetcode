class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n = len(s)        
        # base case
        if n < 10:
            return []
        
        # use sliding window to find each 10 letter sequence
        L = 0
        R = 9
        d = {}
        while R < n:
            cur = s[L:R+1]
            # record each 10 letter sequence in dict with count of number of occurences
            d[cur] = d.get(cur,0)+1
            R += 1
            L += 1
        
        # return all repeated 10 letter sequences
        res = []
        for key in list(d.keys()):
            if d[key]>1:
                res.append(key)
        return res
    