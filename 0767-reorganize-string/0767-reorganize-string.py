class Solution:
    def reorganizeString(self, s: str) -> str:
        # make dict of frequency counts of letters in s
        d = {}
        for c in s:
            d[c] = d.get(c,0)+1
            
        # return "" if not possible
        if max(list(d.values())) > (len(s)+1)/2:
            return ""
        
        # sort s alphabetically        
        s = sorted(s)
        
        # sort s in order of frequency
        s = sorted(s, key = lambda x: d[x])
        
        # rearrange s so that any two adjacent characters are not the same
        h = int(len(s)/2)
        s[1::2], s[::2] = s[:h], s[h:]
        
        # return rearranged s
        return ''.join(s)
        