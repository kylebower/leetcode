class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        
        rows = range(int(s[1]), int(s[4]) + 1)
        cols = self.char_range(s[0], s[3])
        
        for col in cols:
            for row in rows:
                res.append(str(col) + str(row))
        
        return res
    
    def char_range(self, c1, c2):
        for c in range(ord(c1), ord(c2)+1):
            yield chr(c)
