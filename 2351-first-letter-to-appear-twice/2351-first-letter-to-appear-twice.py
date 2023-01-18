class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ds = {}
        for c in s:
            ds[c] = ds.get(c,0) + 1
            if ds[c] == 2:
                return c
