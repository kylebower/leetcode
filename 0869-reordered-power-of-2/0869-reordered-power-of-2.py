class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        m = 1
        while len(str(m)) <= len(str(n)):
            if self.isReorder(m, n):
                return True
            else:
                m *= 2
        return False
    
    def isReorder(self, m: int, n: int) -> bool:
        dm = {}
        dn = {}
        for c in str(m):
            dm[c] = dm.get(c,0)+1
        for c in str(n):
            dn[c] = dn.get(c,0)+1
        return dm == dn
    