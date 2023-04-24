class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # define common dict
        d = {}
        n = len(words)
        
        w0 = words[0]
        for c in w0:
            d[c] = d.get(c,0)+1
        
        for i in range(n-1):
            # make dict for char in new word
            wi = words[i+1]
            dwi = {}
            for c in wi:
                dwi[c] = dwi.get(c,0)+1
            # update common dict
            for c in list(d.keys()):
                if c not in dwi:
                    d.pop(c)
                else:
                    d[c] = min(d[c],dwi[c])
            
        # return result
        print(d)
        res = []
        for c in d:
            for k in range(d[c]):
                res.append(c)
        return res
            
        