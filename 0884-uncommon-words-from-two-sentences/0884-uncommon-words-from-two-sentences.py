class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        split1 = s1.split(" ")
        split2 = s2.split(" ")
        d ={}
        for w in split1 + split2:
            d[w] = d.get(w,0)+1

        res = []
        for w in d:
            if d[w] == 1:
                res.append(w)
                
        return res
        