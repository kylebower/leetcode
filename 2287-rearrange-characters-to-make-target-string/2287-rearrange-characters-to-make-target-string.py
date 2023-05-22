class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ds = {}
        for c in s:
            ds[c] = ds.get(c,0)+1
        dt = {}
        for c in target:
            dt[c] = dt.get(c,0)+1
        
        res = math.inf
        for c in dt:
            copies = ds.get(c,0) // dt[c]
            res = min(res, copies)
        
        return res
        