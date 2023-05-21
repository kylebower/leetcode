class Solution:
    def frequencySort(self, s: str) -> str:
        # make dict of frequencies of each char in s
        d = {}
        for c in s:
            d[c] = d.get(c,0)+1
        
        # sort s based on frequency
        s1 = [[d[c],c] for c in s]
        s1.sort()
        
        # return sorted string
        s2 = [x[1] for x in s1]
        return ''.join(s2[::-1])
    