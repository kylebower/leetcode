class Solution:
    def minDeletions(self, s: str) -> int:
        
        # define dict of count of each char in s
        d = {}
        for c in s:
            d[c] = d.get(c,0)+1
        
        # list frequencies of each char in decreasing order
        freq = list(d.values())
        freq.sort()
        freq = freq[::-1]
        
        # count number of deletions necessary
        res = 0
        n = len(freq)
        for i in range(1,n):
            while freq[i] >= freq[i-1] and freq[i] > 0:
                freq[i] -= 1
                res += 1
        
        # return result
        return res
        